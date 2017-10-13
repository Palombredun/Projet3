#!/usr/bin/env python

import os

os.chdir("./carte")

with open("labyrinthe.txt", "r") as carte:
    labyrinthe = carte.read()
no_line = 0
for letter in labyrinthe:
    if letter == "\n":
        no_line += 1
    
labyrinthe = labyrinthe.replace('\n', '')
no_column = len(labyrinthe) // no_line
   

liste = [ [0]*no_column for i in range(no_line) ]

compteur = 0
for i in range(15):
    for j in range(15):
        liste[i][j] = labyrinthe[compteur]
        compteur += 1
       
print(liste)
