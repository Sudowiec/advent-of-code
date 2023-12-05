import os, sys
from collections import defaultdict

f = open(os.path.join(sys.path[0], "05.txt"), "r")

NUMOFMAPS = 7

seeds = []
seedranges = list(map(int, f.readline().strip()[7:].split(" ")))
print(seedranges)
for i in range(0, len(seedranges), 2):
    for j in range(seedranges[i], seedranges[i] + seedranges[i + 1]):
        seeds.append(j)
print(seeds)
exit()
f.readline()

maps = {}
mapnames = []
for i in range(NUMOFMAPS):
    ranges = []
    mname = f.readline().strip()[:-5]
    mapnames.append(mname)
    l = f.readline().strip()
    while l != "":
        l = list(map(int, l.split(" ")))
        beg = [l[1], l[0]]
        end = [l[1] + l[2] - 1, l[0] + l[2] - 1]
        ranges.append([beg, end])
        l = f.readline().strip()
    maps[mname] = ranges

seedneeds = []
for s in seeds:
    seeddict = {"seed" : s}
    curval = s
    for m in mapnames:
        for r in maps[m]:
            if curval >= r[0][0] and curval <= r[1][0]:
                diff = curval - r[0][0]
                curval = r[0][1] + diff
                break
        seeddict[m.split("-")[2]] = curval
    seedneeds.append(seeddict)
print(seedneeds)

lowest = 999999999
for i in seedneeds:
    if i["location"] < lowest:
        lowest = i["location"]
print(lowest)