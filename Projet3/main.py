#!/usr/bin/env python

import pygame
import sys
from pygame.locals import *
from app import labyrinth as lb
from app import movements

# Initialization of pygame :
pygame.init()

# Rules :
print("*************************************")
print("                                     ")
print("         Saving MacGyver             ")
print("                                     ")
print("*************************************")

print("In this game, you are MacGyver, famous hero of the\nnot so modern times.")
print("In order to pass the guardian (the one with the funny hair), you have")
print("to collect three items randomly located on the map. A needle, a plastic tube")
print("and a bottle of ether should be enough for you to put the guardian to sleep.")
print("But don't be cocky ! Without these tree items you won't be able to defeat")
print("him !\n")
print("In order to move on the map you have to use the arrow keys on your keyboard.")
print("Good Luck !")

# Display of the game :
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
