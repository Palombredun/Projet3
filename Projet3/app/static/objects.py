#!/usr/bin/env python3

import random

def place_objects(labyrinthe, no_line, no column):
    x_true = False
    y_true = False
    z_True = False
    
    while x_true is False and y_true is False and z_true is False:
        x_abs = random.randint(0, no_line)
        x_ord = random.randint(0, no_column)
        if labyrinthe[x_abs][x_ord] == 'o':
            x_true = True
            labyrinthe[x_abs][x_ord] = 'x'
            
        y_abs = random.randint(0, no_line)
        y_ord = random.randint(0, no_column)
        if labyrinthe[y_abs][y_ord] == 'o':
            y_true = True
            labyrinthe[y_abs][y_ord] = 'y'

        z_abs = random.randint(0, no_line)
        z_ord = random.randint(0, no_column)
        if labyrinthe[z_abs][z_ord] == 'o':
            z_true = True
            labyrinthe[z_abs][z_ord] = 'z'
        
    return labyrinthe

def count_objects_obtained(hero_abs, hero_ord, labyrinthe):
    if labyrinthe[hero_abs][hero_ord] == 'x' or labyrinthe[hero_abs][hero_ord] == 'y' \
       labyrinthe[hero_abs][hero_ord] == 'z':
        counter += 1
        labyrinthe[hero_abs][hero_ord] = 'm'
    return labyrinthe
    

    
