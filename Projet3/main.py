#!/usr/bin/env python

import pygame
import sys
from pygame.locals import *
from app import maze
from app import interact

window = maze.Labyrinth()
i, j = 0
while maze.labyrinth[i][j] != 'h':
        i+=1
        j+=1
interact = interact.Interact(self, i, j)

while interact.victory:
    if event.type == KEYDOWN:
        if event.key == K_LEFT:
            interact.hero_position = interact.move_left(maze.labyrinth, interact.hero_position)
            maze.labyrinth[interact.hero_position[0]][interact.hero_position[1]] = 'h'
        elif event.key == K_RIGHT:
            pass
        elif event.key == K_UP:
            pass
        elif event.key == K_DOWN:
            interact.hero_position = interact.move_down(maze.labyrinth, interact.hero_position)
            maze.labyrinth[interact.hero_position[0]][interact.hero_position[1]] = 'h'
        pygame.display.flip()
    victory = int(input())


print("Félicitations ! Vous avez gagné !")
