import os, sys

LENGTH = 726

f = open(os.path.join(sys.path[0], "08.txt"), "r")

dirs = f.readline().strip()
dirLen = len(dirs)
f.readline()

graph = {}
for i in range(LENGTH):
    t = f.readline().strip().split(" ")
    c = t[2].split(", ")
    graph[t[0]] = {"L" : t[2][1:-1], "R" : t[3][:-1]}

steps = 0
cur = "AAA"
i = 0
while True:
    curstep = dirs[i]
    steps += 1
    cur = graph[cur][curstep]
    if cur == "ZZZ":
        break
    i = (i + 1) % dirLen
print(steps)