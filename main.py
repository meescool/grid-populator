'''
This program is for populating a grid with 4 set of coordinates for each
square inside of the grid. 
Will be using this to better facilitate my Tic Tac Toe PG game

Author: Marcela Estrada
Date: 1/6/2022
'''

import pygame, sys

import grid as g

pygame.init

size = (500,500)

white = 255,255,255

red = 255,0,0

scr = pygame.display.set_mode((size))


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    plots = g.geometry()

    for p in plots:
        box = pygame.Rect(p[0][0],p[0][1],p[3][0],p[3][1])
        # box = pygame.Rect(50,50,183,183)
        pygame.draw.rect(scr,(255,255,),(box),2)
    # box = pygame.Rect(50,50,183,183)
    # pygame.draw.rect(scr,white,(box),2)

    

    pygame.display.update()