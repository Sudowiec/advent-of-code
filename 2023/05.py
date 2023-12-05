import os, sys
from collections import defaultdict

f = open(os.path.join(sys.path[0], "05.txt"), "r")

NUMOFMAPS = 7

seeds = list(map(int, f.readline().strip()[7:].split(" ")))
f.readline()

maps = defaultdict(lambda : {})
mapnames = []
for m in range(NUMOFMAPS):
    curmap = f.readline().strip()[:-5]
    mapnames.append(curmap)
    l = f.readline().strip()
    while l != "":
        l = list(map(int, l.split(" ")))
        for i in range(l[2]):
            maps[curmap][l[1] + i] = l[0] + i
        l = f.readline().strip()

seedneeds = []
for seed in seeds:
    seeddict = {"seed" : seed}
    curval = seed
    curname = "seed"
    for m in mapnames:
        if curval in maps[m].keys():
            curval = maps[m][curval]
        curname = m.split("-")[2]
        seeddict[curname] = curval
    seedneeds.append(seeddict)
print(seedneeds)

lowest = 999999999
for i in seedneeds:
    if i["location"] < lowest:
        lowest = i["location"]
print(lowest)