#!/usr/bin/env python3

import pygame
from pygame.locals import *
from app import labyrinth as lb

class Movements(lb.Labyrinth):
    def move_left(self):
        self.test_position[0] = self.hero_position[0]-1
        self.test_position[1] = self.hero_position[1]
        #test if the position is a wall :
        if self.is_wall(self.test_position) is False:
            return self.hero_position
            pass
        else:
            #is_object(labyrinth, test_position)
            # if the case to go is not a wall, the hero_position changes :
            self.labyrinth[self.hero_position[0]][self.hero_position[1]] = 'o'
            self.graphicLabyrinth.blit( \
                self.path, (32*self.hero_position[0], 32*self.hero_position[1]) )
            self.hero_position = self.test_position
            self.labyrinth[self.hero_position[0]][self.hero_position[1]] = 'h'
            self.graphicLabyrinth.blit( \
                self.hero, (32*self.hero_position[0], 32*self.hero_position[1]) )
    def move_right(self):
        self.test_position[0] = self.hero_position[0]+1
        self.test_position[1] = self.hero_position[1]
        #test if the position is a wall :
        if self.is_wall(self.test_position) is True:
            #return self.hero_position
            pass
        else:
            #is_object(labyrinth, test_position)
            # if the case to go is not a wall, the hero_position changes :
            self.labyrinth[self.hero_position[0]][self.hero_position[1]] = 'o'
            self.graphicLabyrinth.blit( \
                self.path, (32*self.hero_position[0], 32*self.hero_position[1]) )
            self.hero_position = self.test_position
            self.labyrinth[self.hero_position[0]][self.hero_position[1]] = 'h'
            self.graphicLabyrinth.blit( \
                self.hero, (32*self.hero_position[0], 32*self.hero_position[1]) )
    def move_up(self):
        pass
    def move_down(self):
        pass
    def is_wall(self, hero_position):
        if self.labyrinth[test_position[0]][test_position[1]] == 'm':
            return True
    def is_object(self, test_position):
        if labyrinth[test_position[0]][test_position[1]] in 'npe':
            self.objects_counter(labyrinth, hero_position)
    def objects_counter(self):
        pass
    def is_victory(self, objects_counter, hero_position):
        pass
    def __init__(self):
        lb.Labyrinth.__init__(self)
        self.test_position = [0,0]
        self.victory = 1 # value =  0 when all the conditions are met
        self.objects = 0 #number of objects
