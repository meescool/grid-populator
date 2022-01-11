'''
!!! EPILEPSY WARNING: Lot's of flashing colors !!!

This program is for populating a grid with 4 set of coordinates for each
square inside of the grid. 
Will be using this to better facilitate my Tic Tac Toe PG game

Author: Marcela Estrada
Date: 1/6/2022
'''

import pygame, sys

from pygame.constants import MOUSEBUTTONDOWN

import grid as g

pygame.init

size = (500,500)

white = 255,255,255

red = 255,0,0

scr = pygame.display.set_mode((size))

clock = pygame.time.Clock()
running = True

change = True
i = 0
k = 0
p = 0
pChange = True
while running:
    pygame.Surface.fill(scr, (255,255,255))
    clock.tick(7)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            k+=1
            if k == 3:
                k = 0

    plots = g.geometry()


    if change == True:
        i+= 5
    else:
        i-= 5
    if i >= 255:
        change = False
        i = 255
    if i <= 0:
        change = True
        i = 0
    bounds = pygame.Rect(plots[p][0],plots[p][1],plots[p][2],plots[p][3])
    color = ()
    if k == 0:
        color = (255,255,i)
    elif k ==1:
        color = (255,i,255)
    else:
        color = (i,255,255)
    box = pygame.draw.rect(scr,color,(bounds),0)

    if pChange == True:
        p+=1
    else:
        p-=1
    if p == 8:
        pChange = False
    if p == 0:
        pChange = True
    

    # for p in plots:
    #     if change == True:
    #         i+= 90
    #     else:
    #         i-= 90
    #     if i >= 255:
    #         change = False
    #         i = 255
    #     if i <= 0:
    #         change = True
    #         i = 0
    #     bounds = pygame.Rect(p[0],p[1],p[2],p[3])
    #     color = ()
    #     if k == 0:
    #         color = (255,255,i)
    #     elif k ==1:
    #         color = (255,i,255)
    #     else:
    #         color = (i,255,255)
    #     box = pygame.draw.rect(scr,color,(bounds),0)
        

    pygame.display.update()