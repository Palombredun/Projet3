#!/usr/bin/env python

import pygame
import sys
from pygame.locals import *
from app import labyrinth as lb
from app import movements

# Initialization of pygame :
pygame.init()

# Initialization of the window :

mvt = movements.Movements()
victory = 1
while victory:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                mvt.move_left()
            elif event.key == K_RIGHT:
                mvt.move_right()
            elif event.key == K_UP:
                mvt.move_up()
            elif event.key == K_DOWN:
                mvt.move_down()
    pygame.display.flip()
    state = mvt.is_victory()
    if state == 1:
        print("Félicitations ! Vous avez gagné !")
        break
    elif state == -1:
        print("Vous avez perdu, il vous manquait des objets")
        break
    elif state == 0:
        continue


print("Félicitations ! Vous avez gagné !")
