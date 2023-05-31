import os
import time
FANCYDISPLAY = True
f = open("2022/14.txt")
lowestx = 9999999
highestx = 0
lowesty = 9999999
highesty = 0
paths = []
while True:
    inp = f.readline().strip()
    if inp == "":
        break
    inp = inp.split(" -> ")
    for i in inp:
        x = int(i.split(",")[0])
        y = int(i.split(",")[1])
        if x < lowestx:
            lowestx = x
        if x > highestx:
            highestx = x
        if y < lowesty:
            lowesty = y
        if y > highesty:
            highesty = y
    paths.append(inp)
lowestx -= 50
highestx += 50
cave = [["." for j in range(highestx - lowestx + 1)] for i in range(highesty + 4)]

def checkdir(a, b):
    if a - b < 0:
        return -1
    else:
        return 1

for path in paths:
    cur = path[0]
    curx = int(cur.split(",")[0]) - lowestx
    cury = int(cur.split(",")[1])
    cave[cury][curx] = "#"
    for j in range(1, len(path)):
        newx = int(path[j].split(",")[0]) - lowestx
        newy = int(path[j].split(",")[1])
        for i in range(curx, newx + checkdir(newx, curx), checkdir(newx, curx)):
            cave[newy][i] = "#"
        for i in range(cury, newy + checkdir(newy, cury), checkdir(newy, cury)):
            cave[i][newx] = "#"
        curx = newx
        cury = newy
cave[highesty + 2] = ["#" for i in range(highestx - lowestx + 1)]

def moveSand(x, y):
    cave[y][x] = "."
    #down
    if cave[y + 1][x] == ".":
        cave[y + 1][x] = "o"
        return [x, y + 1]
    # left
    if cave[y + 1][x - 1] == ".":
        cave[y + 1][x - 1] = "o"
        return [x - 1, y + 1]
    # right
    if cave[y + 1][x + 1] == ".":
        cave[y + 1][x + 1] = "o"
        return [x + 1, y + 1]
    cave[y][x] = "o"
    return "rests"

sandCount = 0
while True:
    sx = 500 - lowestx
    sy = 0
    while True:
        tmp = moveSand(sx, sy)
        if FANCYDISPLAY:
            os.system("cls")
            for i in cave:
                print("".join(i))
            time.sleep(0.01)
        if tmp == "rests":
            sandCount += 1
            break
        sx = tmp[0]
        sy = tmp[1]
        if sy > highesty:
            print(sandCount)
            exit()
