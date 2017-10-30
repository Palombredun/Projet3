#!/usr/bin/env python
# -*-coding:Utf-8 -*

"""File used to run the game."""

import pygame
from pygame.locals import *
from app import movements


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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                mvt.move_left()
            elif event.key == pygame.K_RIGHT:
                mvt.move_right()
            elif event.key == pygame.K_UP:
                mvt.move_up()
            elif event.key == pygame.K_DOWN:
                mvt.move_down()
    pygame.display.flip()
    state = mvt.is_victory()
    if state == 1:
        print("Congratulations ! You have won !")
        break
    elif state == -1:
        print("You lost, you did not have all the items needed.")
        break
    elif state == 0:
        continue
