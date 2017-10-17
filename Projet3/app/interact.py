#!/usr/bin/env python3

import pygame
from pygame.locals import *
from maze import Labyrinth

class Interact:
    def move_left(self, labyrinth, hero_position):
        test_position = labyrinth[hero_position[0]-1][hero_position[1]]
        if self.is_wall(labyrinth, test_position):
            return hero_position
            pass
        else:
            is_object(labyrinth, test_position)
            maze.labyrinth[hero_position[0]][hero_position[1]] = 'm'
            maze.labyrinth[test_position[0]][test_position[1]] = 'h'
            return hero_position
    def move_right(self):
        pass
    def move_up(self):
        pass
    def move_down(self):
        test_position = labyrinth[hero_position[0]][hero_position[1]-1]
        if self.is_wall(labyrinth, test_position):
            return hero_position
            pass
        else:
            is_object(labyrinth, test_position)

            return hero_position
    def is_wall(self, labyrinth, test_position):
        if labyrinth[test_position[0]][test_position[1]] == 'm':
            return False
    def is_object(self, labyrinth, test_position):
        if labyrinth[test_position[0]][test_position[1]] in 'npe':
            self.objects_counter(labyrinth, hero_position)
    def objects_counter(self):
        pass
    def is_victory(self, objects_counter, hero_position):
        pass
    def __init__(self, hero_x, hero_y):
        pygame.init()
        interact.hero_position = maze.hero.get_rect(center=(32*i-16, 32*j-16))
        self.hero_position = []
        self.test_position = []
        self.victory = 1
