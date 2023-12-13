import os, sys
import math

LENGTH = 726

f = open(os.path.join(sys.path[0], "08.txt"), "r")

dirs = f.readline().strip()
dirLen = len(dirs)
f.readline()

graph = {}
curs = []
for i in range(LENGTH):
    t = f.readline().strip().split(" ")
    c = t[2].split(", ")
    graph[t[0]] = {"L" : t[2][1:-1], "R" : t[3][:-1]}
    if t[0][2] == "A":
        curs.append(t[0])

multisteps = []
for c in curs:
    cur = c
    steps = 0
    i = 0
    while True:
        curstep = dirs[i]
        steps += 1
        cur = graph[cur][curstep]
        if cur[2] == "Z":
            break
        i = (i + 1) % dirLen
    multisteps.append(steps)
print(math.lcm(multisteps[0], multisteps[1], multisteps[2], multisteps[3], multisteps[4], multisteps[5]))