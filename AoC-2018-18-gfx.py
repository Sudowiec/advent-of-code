import copy
import time
import os
import pygame
clear = lambda: os.system('cls')
matrix = []
side = 50
pygame.init()
sq=5
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
    # clear()
    new_matrix = copy.deepcopy(matrix)

    matrix.insert(0, [ "-" for i in range(side)])
    matrix.append([ "-" for i in range(side)])
    for i in matrix:
        i.insert(0, "-")
        i.append("-")

    for y in range(1, side + 1):
        for x in range(1, side + 1):
            objects = {"|" : 0, "#" : 0, "." : 0, "-" : 0}
            objects[matrix[y][x - 1]] += 1
            objects[matrix[y + 1][x - 1]] += 1
            objects[matrix[y + 1][x]] += 1
            objects[matrix[y + 1][x + 1]] += 1
            objects[matrix[y][x + 1]] += 1
            objects[matrix[y - 1][x + 1]] += 1
            objects[matrix[y - 1][x]] += 1
            objects[matrix[y - 1][x - 1]] += 1

            if matrix[y][x] == "." and objects["|"] >= 3:
                new_matrix[y - 1][x - 1] = "|"
            if matrix[y][x] == "|" and objects["#"] >= 3:
                new_matrix[y - 1][x - 1] = "#"
            if matrix[y][x] == "#" and (objects["#"] == 0 or objects["|"] == 0):
                new_matrix[y - 1][x - 1] = "."
    # time.sleep(0.05)
    for y in range(side):
        for x in range(side):
            if new_matrix[x][y] == "#":
                pygame.draw.rect(windowSurface, RED, (sq*x, sq*y, sq*x+sq-1, sq*y+sq-1))
                #pixArray[x][y] = BLACK
            elif new_matrix[x][y] == "|":
                pygame.draw.rect(windowSurface, GREEN, (sq*x, sq*y, sq*x+sq-1, sq*y+sq-1))
                #pixArray[x][y] = WHITE
            else:
                pygame.draw.rect(windowSurface, BLACK, (sq * x, sq * y, sq * x + sq - 1, sq * y + sq - 1))
                # pixArray[x][y] = WHITE
    pygame.event.get()
    pygame.display.update()
    matrix = copy.deepcopy(new_matrix)
    print(step)
trees = 0
lumbs = 0
for i in matrix:
    for j in i:
        if j == "#":
            lumbs += 1
        elif j == "|":
            trees += 1
print(trees * lumbs)