#!/usr/bin/env python3

import pygame
from pygame.locals import *
import os
import random


#initialization of the pygame library


class Labyrinth:
    """Initialization of the graphic interface by using the resources
    located in the folder 'resources'. The size of the graphic interface is
    defined by the size of the labyrinth (here 15*15 sprites) and the size
    of the sprites (here 32*32).

    When the class is called, the 3 objects needed for the victory are randomly
    place on the labyrinth, then the graphic interfac is displayed, but it has
    to be in a loop (usually while), or else it will just appear briefly on
    the screen.
    """
    def load_labyrinth(self, raw_labyrinth):
        """Generation of a 2d list called labyrinth which will be used
        for track the hero's position"""
        no_row = 0
        no_column = 0
        for letter in raw_labyrinth:
            if letter == "\n":
                no_row += 1
        no_column = len(raw_labyrinth)//no_row
        # strip 'raw_labyrinth' from the line breaks
        raw_labyrinth = raw_labyrinth.replace('\n', '')

        # 'labyrinth' is a 2 dimensions list with 'no_row' rows
        # and 'no_column' columns (here 15*15)
        labyrinth = [ [0]*no_column for i in range(no_row) ]
        counter = 0
        for i in range(15):
            for j in range(15):
                labyrinth[i][j] = raw_labyrinth[counter]
                counter += 1
        lst = [labyrinth, no_row, no_column]
        return lst

    def place_objects(self, labyrinth, no_row, no_column):
        """Placement of the three objects needed for the victory
        and the management of their counter display"""
        needle_true = 1
        plastic_tube_true = 1
        ether_true = 1

        while needle_true:
            x_row = random.randint(0, no_row-1)
            x_ord = random.randint(0, no_column-1)
            if labyrinth[x_row][x_ord] == 'o':
                self.labyrinth[x_row][x_ord] = 'n'
                needle_true = 0
        while plastic_tube_true:
            y_row = random.randint(0, no_row-1)
            y_ord = random.randint(0, no_column-1)
            if labyrinth[y_row][y_ord] == 'o':
                self.labyrinth[y_row][y_ord] = 'p'
                plastic_tube_true = 0
        while ether_true:
            z_row = random.randint(0, no_row-1)
            z_ord = random.randint(0, no_column-1)
            if labyrinth[z_row][z_ord] == 'o':
                self.labyrinth[z_row][z_ord] = 'e'
                ether_true = 0


        return labyrinth

    def __init__(self):
        """Printing of the graphic interface using the images loaded
        from the resources folder"""

        # Generation of labyrinth as a 2d list :
        os.chdir("./resources/map")
        with open("labyrinth.txt", "r") as tmp:
            raw_labyrinth = tmp.read()
        tmp = self.load_labyrinth(raw_labyrinth)
        self.labyrinth = tmp[0]
        self.no_row = tmp[1]
        self.no_column = tmp[2]


        # The labyrinth is updated with the three objects placed randomly
        self.labyrinth = self.place_objects(self.labyrinth, self.no_row, self.no_column)

        #Creation of the window :
        pygame.init()
        self.graphicLabyrinth = pygame.display.set_mode((32*self.no_row, 32*self.no_column))

        # Here we load all the images from the folder 'resources'
        # to display the game
        os.chdir("../images")
        self.wall = pygame.image.load("wall.jpg").convert()
        self.path = pygame.image.load("path.jpg").convert()
        self.hero = pygame.image.load("macgyver.png").convert_alpha()
        self.guardian = pygame.image.load("guardian.png").convert_alpha()
        self.needle = pygame.image.load("needle.png").convert_alpha()
        self.plastic_tube = pygame.image.load("plastic_tube.png").convert_alpha()
        self.ether = pygame.image.load("ether.png").convert_alpha()

        for i in range(self.no_row):
            for j in range(self.no_column):
                if self.labyrinth[i][j] == 'm':
                    self.graphicLabyrinth.blit(self.wall, (32*i, 32*j))
                else:
                    self.graphicLabyrinth.blit(self.path, (32*i, 32*j))
        for i in range(self.no_row):
            for j in range(self.no_column):
                if self.labyrinth[i][j] == 'h':
                    self.graphicLabyrinth.blit(self.hero, (32*i, 32*j))
                elif self.labyrinth[i][j] == 'v':
                    self.graphicLabyrinth.blit(self.guardian, (32*i, 32*j))
                elif self.labyrinth[i][j] == 'n': # n for needle
                    self.graphicLabyrinth.blit(self.needle, (32*i, 32*j))
                elif self.labyrinth[i][j] == 'p': # p for plastic_tube
                    self.graphicLabyrinth.blit(self.plastic_tube, (32*i, 32*j))
                elif self.labyrinth[i][j] == 'e': # e for ether (and f for fake)
                    self.graphicLabyrinth.blit(self.ether, (32*i, 32*j))
        # Display of the labyrinth :
        pygame.display.flip()
