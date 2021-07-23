import copy
import time

import pygame, sys
from pygame.locals import *

pygame.init()

matrix = []
side = 100

sq=3
windowSurface = pygame.display.set_mode((sq*(side+1), sq*(side+1)), 0, 32)
# pixArray = pygame.PixelArray(windowSurface)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

while True:
    try:
        matrix.append(list(input()))
    except EOFError:
        break

for step in range(10000):
#    clear()
    new_matrix = copy.deepcopy(matrix)

    matrix.insert(0, [ "-" for i in range(side)])
    matrix.append([ "-" for i in range(side)])
    for i in matrix:
        i.insert(0, "-")
        i.append("-")

    for y in range(1, side + 1):
        for x in range(1, side + 1):
            neighbours = 0
            if matrix[y][x - 1] == "#": # left
                neighbours += 1
            if matrix[y + 1][x - 1] == "#": # left-down
                neighbours += 1
            if matrix[y + 1][x] == "#": # down
                neighbours += 1
            if matrix[y + 1][x + 1] == "#": # right-down
                neighbours += 1
            if matrix[y][x + 1] == "#": # right
                neighbours += 1
            if matrix[y - 1][x + 1] == "#": # right-up
                neighbours += 1
            if matrix[y - 1][x] == "#": # up
                neighbours += 1
            if matrix[y - 1][x - 1] == "#": # left-up
                neighbours += 1

            if matrix[y][x] == "#" and (neighbours != 3 and neighbours != 2):
                new_matrix[y - 1][x - 1] = "."
            if matrix[y][x] == "." and neighbours == 3:
                new_matrix[y - 1][x - 1] = "#"
            new_matrix[0][0] = "#"
            new_matrix[0][side - 1] = "#"
            new_matrix[side - 1][0] = "#"
            new_matrix[side - 1][side - 1] = "#"


    for y in range(1, side + 1):
        for x in range(1, side + 1):
            if matrix[x][y] == "#":
                pygame.draw.rect(windowSurface, RED, (sq*x, sq*y, sq*x+sq-1, sq*y+sq-1))
                #pixArray[x][y] = BLACK
            else:
                pygame.draw.rect(windowSurface, BLACK, (sq*x, sq*y, sq*x+sq-1, sq*y+sq-1))
                #pixArray[x][y] = WHITE
    pygame.event.get()
    pygame.display.update()

    #time.sleep(0.05)


    matrix = copy.deepcopy(new_matrix)
counter = 0
for i in matrix:
    for j in i:
        if j == "#":
            counter += 1
print(counter)