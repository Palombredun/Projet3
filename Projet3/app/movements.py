#!/usr/bin/env python3

import pygame
from pygame.locals import *
from app import labyrinth as lb

class Movements(lb.Labyrinth):
    def move_left(self):
        self.test_position = self.hero_position[:]
        self.test_position[0] -= 1
        #test if the position is a wall :
        if self.is_wall(self.test_position) is True:
            pass
        else:
            self.is_object(self.test_position)
            # if the case to go is not a wall, the hero_position changes :
            self.labyrinth[self.hero_position[0]][self.hero_position[1]] = 'o'
            self.graphicLabyrinth.blit( \
                self.path, (32*self.hero_position[0], 32*self.hero_position[1]) )
            self.hero_position[0] -= 1
            self.labyrinth[self.hero_position[0]][self.hero_position[1]] = 'h'
            self.graphicLabyrinth.blit( \
                self.hero, (32*self.hero_position[0], 32*self.hero_position[1]) )
    def move_right(self):
        self.test_position = self.hero_position[:]
        self.test_position[0] += 1
        #test if the position is a wall :
        if self.is_wall(self.test_position) is True:
            pass
        else:
            self.is_object(self.test_position)
            # if the case to go is not a wall, the hero_position changes :
            self.labyrinth[self.hero_position[0]][self.hero_position[1]] = 'o'
            self.graphicLabyrinth.blit( \
                self.path, (32*self.hero_position[0], 32*self.hero_position[1]) )
            self.hero_position[0] += 1
            self.labyrinth[self.hero_position[0]][self.hero_position[1]] = 'h'
            self.graphicLabyrinth.blit( \
                self.hero, (32*self.hero_position[0], 32*self.hero_position[1]) )
    def move_up(self):
        self.test_position = self.hero_position[:]
        self.test_position[1] -= 1
        #test if the position is a wall :
        if self.is_wall(self.test_position) is True:
            pass
        else:
            self.is_object(self.test_position)
            # if the case to go is not a wall, the hero_position changes :
            self.labyrinth[self.hero_position[0]][self.hero_position[1]] = 'o'
            self.graphicLabyrinth.blit( \
                self.path, (32*self.hero_position[0], 32*self.hero_position[1]) )
            self.hero_position[1] -= 1
            self.labyrinth[self.hero_position[0]][self.hero_position[1]] = 'h'
            self.graphicLabyrinth.blit( \
                self.hero, (32*self.hero_position[0], 32*self.hero_position[1]) )
    def move_down(self):
        self.test_position = self.hero_position[:]
        self.test_position[1] += 1
        #test if the position is a wall :
        if self.is_wall(self.test_position) is True:
            pass
        else:
            # test if the case is an object :
            self.is_object(self.test_position)
            # if the case to go is not a wall, the hero_position changes :
            self.labyrinth[self.hero_position[0]][self.hero_position[1]] = 'o'
            self.graphicLabyrinth.blit( \
                self.path, (32*self.hero_position[0], 32*self.hero_position[1]) )
            self.hero_position[1] += 1
            self.labyrinth[self.hero_position[0]][self.hero_position[1]] = 'h'
            self.graphicLabyrinth.blit( \
                self.hero, (32*self.hero_position[0], 32*self.hero_position[1]) )
    def is_wall(self, test_position):
        if self.labyrinth[test_position[0]][test_position[1]] == 'm':
            return True
        else:
            return False
    def is_object(self, test_position):
        if self.labyrinth[test_position[0]][test_position[1]] in 'npe':
            self.objects += 1
            print(self.objects)
    def is_victory(self):
        if (self.objects == 3) and (self.hero_position == self.guardian_position):
            print("1")
            return 1
        elif (self.objects < 3) and (self.hero_position == self.guardian_position):
            print("-1")
            return -1
        elif self.hero_position != self.guardian_position:
            return 0
    def __init__(self):
        lb.Labyrinth.__init__(self)
        self.test_position = []
        self.victory = 1 # value =  0 when all the conditions are met
        self.objects = 0 #number of objects
