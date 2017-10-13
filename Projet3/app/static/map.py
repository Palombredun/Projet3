#!/usr/bin/env python3

import pygame


from pygame.locals import *

#initialization of the pygame library
pygame.init()
fenetre = pygame.display.set_mode((640, 480))

class graphicInterface:
        
    def __init__(labyrinth, no_line, no_column):
        pygame.init()
        self.graphicLab = pygame.display.set_mode((32*no_line, 32*no_column))
        self.wall = pygame.image.load("wall.jpg").convert()
        self.path = pygame.image.load("path.jpg").convert()
        self.hero = pygame.image.load("macgyver.png").convert_alpha()
        self.guardian = pygame.image.load("guardian.jpg").convert_alpha()
        self.object1 = pygame.image.load("object1.jpg").convert_alpha()
        self.object2 = pygame.image.load("object2.jpg").convert_alpha()
        self.object3 = pygame.image.load("object3.jpg").convert_alpha()
        
        for i in range(no_line):
            for j in range(no_column):
                if labyrinth[i][j] == 'm':
                    self.graphicLab.blit(self.wall, (32*i, 32*j))
                elif labyrinth[i][j] == 'o'
                    self.graphicLab.blit(self.path, (32*i, 32*j))
                elif labyrinth[i][j] == 'h':
                     self.graphicLab.blit(self.hero, (32*i, 32*j))
                elif labyrinth[i][j] == 'v':
                     self.graphicLab.blit(self.guardian, (32*i, 32*j))
                elif labyrinthe[i][j] == 'object1':
                    self.graphicLab.blit(self.x, (32*i, 32*j))
                elif labyrinthe[i][j] == 'object2':
                    self.graphicLab.blit(self.x, (32*i, 32*j))
                elif labyrinthe[i][j] == 'object3':
                    self.graphicLab.blit(self.x, (32*i, 32*j))

    def update_map(hero_x, hero_y)
                    
