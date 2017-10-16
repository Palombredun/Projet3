#!/usr/bin/env python

import pygame
import sys
from pygame.locals import *
from app import maze


victory = 1

window = maze.Labyrinth()

while victory:
    """
    if event.type == KEYDOWN:
        if event.key == K_LEFT:
            pass
        elif event.key == K_RIGHT:
            pass
        elif event.key == K_UP:
            pass
        elif event.key == K_DOWN:
            pass
    """
    victory = int(input())


print("Félicitations ! Vous avez gagné !")
