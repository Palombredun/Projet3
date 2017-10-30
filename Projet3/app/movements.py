#!/usr/bin/env python3
# -*-coding:Utf-8 -*

from pygame.locals import *
from app import labyrinth as lb

class Movements(lb.Labyrinth):
    """
    This class is in charge of the movements of the character in the list
    labyrinth, before displaying them on the screen.
    When an event is detected (supposing it is one of the four arrow keys),
    the destination is tested : if it is a wall, nothing happens, if it is an
    object, the number of objects possessed by the player is incremented and
    updated. After a movement, the position of the hero is tested in order
    to know if he stands before the guardian with the three objetcs or not.
    """
    def move_left(self):
        """Move the hero on the left if is not a wall"""
        self.test_position = self.hero_position[:]
        self.test_position[0] -= 1
        #test if the position is a wall :
        if self.is_wall(self.test_position) is True:
            pass
        else:
            self.is_object(self.test_position)
            # if the case to go is not a wall, the hero_position changes :
            self.labyrinth[self.hero_position[0]][self.hero_position[1]] = 'o'
            self.graphicLabyrinth.blit(self.path,
                (32*self.hero_position[0], 32*self.hero_position[1]))
            self.hero_position[0] -= 1
            self.labyrinth[self.hero_position[0]][self.hero_position[1]] = 'h'
            self.graphicLabyrinth.blit(self.hero,
                (32*self.hero_position[0], 32*self.hero_position[1]))
    def move_right(self):
        """Move the hero on the right if is not a wall"""
        self.test_position = self.hero_position[:]
        self.test_position[0] += 1
        #test if the position is a wall :
        if self.is_wall(self.test_position) is True:
            pass
        else:
            self.is_object(self.test_position)
            # if the case to go is not a wall, the hero_position changes :
            self.labyrinth[self.hero_position[0]][self.hero_position[1]] = 'o'
            self.graphicLabyrinth.blit(self.path,
                (32*self.hero_position[0], 32*self.hero_position[1]))
            self.hero_position[0] += 1
            self.labyrinth[self.hero_position[0]][self.hero_position[1]] = 'h'
            self.graphicLabyrinth.blit(self.hero,
                (32*self.hero_position[0], 32*self.hero_position[1]))
    def move_up(self):
        """Move the hero up if is not a wall"""
        self.test_position = self.hero_position[:]
        self.test_position[1] -= 1
        #test if the position is a wall :
        if self.is_wall(self.test_position) is True:
            pass
        else:
            self.is_object(self.test_position)
            # if the case to go is not a wall, the hero_position changes :
            self.labyrinth[self.hero_position[0]][self.hero_position[1]] = 'o'
            self.graphicLabyrinth.blit(self.path,
                (32*self.hero_position[0], 32*self.hero_position[1]))
            self.hero_position[1] -= 1
            self.labyrinth[self.hero_position[0]][self.hero_position[1]] = 'h'
            self.graphicLabyrinth.blit(self.hero,
                (32*self.hero_position[0], 32*self.hero_position[1]))
    def move_down(self):
        """Move the hero down if is not a wall"""
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
            self.graphicLabyrinth.blit(self.path,
                (32*self.hero_position[0], 32*self.hero_position[1]))
            self.hero_position[1] += 1
            self.labyrinth[self.hero_position[0]][self.hero_position[1]] = 'h'
            self.graphicLabyrinth.blit(self.hero,
                (32*self.hero_position[0], 32*self.hero_position[1]))
    def is_wall(self, test_position):
        """if test_position is a wall, return True"""
        if self.labyrinth[test_position[0]][test_position[1]] == 'm':
            return True
        else:
            return False
    def is_object(self, test_position):
        """if test_position is an object, increment the number of objects
        and display the new value on the console"""
        if self.labyrinth[test_position[0]][test_position[1]] in 'npe':
            self.objects += 1
            print("You possess : ", self.objects, " item on the 3 required.")
    def is_victory(self):
        """If the hero possesses all three objects and stands before the
        guardian, the game is finished, the player has won. However, if he
        hasn't collected the three objects and still stands before the guardian,
        the player has lost.
        Finally, if the player has not yet collected the three items and is
        not in front of the guardian, nothing happens.
        """
        if (self.objects == 3 and
            self.hero_position == self.guardian_position):
            return 1
        elif (self.objects < 3 and
              self.hero_position == self.guardian_position):
            return -1
        elif self.hero_position != self.guardian_position:
            return 0
    def __init__(self):
        lb.Labyrinth.__init__(self)
        self.test_position = []
        self.victory = 1 # value =  0 when all the conditions are met
        self.objects = 0 #number of objects
