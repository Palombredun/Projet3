#!/usr/bin/env python3

import pygame
from pygame.locals import *

class Interactions:
    def move_left(self, labyrinth, hero_position):
        self.is_object()
        pass
    def move_right:
        pass
    def move_up:
        pass
    def move_down:
        pass
    def is_wall(self):
        pass
    def is_object(self, labyrinth, hero_position):
        if labyrinth[position_x][position_y] in 'npe':
            self.objects_counter(labyrinth, hero_position)
            return True
        else:
            return False
    def objects_counter:
        pass
    def is_victory:
        pass
    def __init__(self):
        hero_position=[]
