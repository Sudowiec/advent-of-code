import re
import time
import copy
pos = []
vel = []
maxup = 0
maxdown = 0
maxleft = 0
maxright = 0

def printgrid(matrix):
    for i in matrix:
        print("".join(i))

while True:
    try:
        inp = input()
    except EOFError:
        break

    mo = re.match(r"position=<(.+), (.+)> velocity=<(.+), (.+)>", inp)
    pos.append([int(mo.group(1).strip()), int(mo.group(2).strip())])
    vel.append([int(mo.group(3).strip()), int(mo.group(4).strip())])

    if int(mo.group(1)) > 0 and int(mo.group(1)) > maxright:
        maxright = int(mo.group(1))
    if int(mo.group(1)) < 0 and int(mo.group(1)) < maxleft:
        maxleft = int(mo.group(1))
    if int(mo.group(2)) > 0 and int(mo.group(2)) > maxdown:
        maxdown = int(mo.group(2))
    if int(mo.group(2)) < 0 and int(mo.group(2)) < maxup:
        maxup = int(mo.group(2))
print(pos)
print(vel)
print(maxup, maxdown, maxleft, maxright)

lenx = abs(maxleft) + abs(maxright) + 1
leny = abs(maxup) + abs(maxdown) + 1
print(lenx, leny)

second = 0
while True:
    maxup = 0
    maxdown = 0
    maxleft = 0
    maxright = 0
    for i in pos:
        if i[0] > maxright:
            maxright = i[0]
        if i[0] < maxleft:
            maxleft = i[0]
        if i[1] > maxdown:
            maxdown = i[1]
        if i[1] < maxup:
            maxup = i[1]
    lenx = abs(maxleft - maxright) + 1
    leny = abs(maxup - maxdown) + 1
    print(lenx, leny)
    for i in range(len(pos)):
        pos[i][0] += vel[i][0]
        pos[i][1] += vel[i][1]
    if lenx < 220 and leny < 130:
        grid = [["." for j in range(220)] for i in range(130)]
        for i in pos:
            grid[i[1] + abs(maxup)][i[0] + abs(maxleft)] = "#"
        printgrid(grid)
        print(second)
        print()
    second += 1

