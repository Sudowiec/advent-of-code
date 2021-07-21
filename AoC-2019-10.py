grid = []
epsilon = 0.00001
import math
while True:
    try:
        grid.append(list(input()))
    except EOFError:
        break
print(grid)
lenx = len(grid[0])
leny = len(grid)

lookouts = {}
for mainy in range(leny):
    for mainx in range(lenx):
        if grid[mainy][mainx] == ".":
            continue

        atans = {}
        for y in range(leny):
            for x in range(lenx):
                if grid[y][x] == "." or (y == mainy and x == mainx):
                    continue
                tcx = mainx - x
                tcy = mainy - y
                atans[math.atan2(tcy, tcx)] = 1
                # print(mainx, mainy, x, y, tcx, tcy, math.atan2(tcy, tcx))
        lookouts[str(mainx) + ", " + str(mainy)] = len(atans)
print(lookouts)
lookout = max(lookouts.values())
lookx = 0
looky = 0
for i in lookouts:
    if lookouts[i] == lookout:
        var = i.split(",")
        lookx = int(var[0])
        looky = int(var[1])
print(lookout, lookx, looky)
laser = math.pi / 2
print(laser)

tovapor = {}
rayhash = {}
for y in range(leny):
    for x in range(lenx):
        if grid[y][x] == "." or (y == looky and x == lookx):
            continue
        tcx = x - lookx
        tcy = looky - y
        ray = math.sqrt(tcx**2 + tcy**2)
        rayhash[str(x) + ", " + str(y)] = ray
        # tovapor[str(x) + ", " + str(y)] = math.atan2(-tcx, -tcy)
        var = math.atan2(tcx, tcy)
        if var < 0:
            var += math.pi * 2
        tovapor[str(x) + ", " + str(y)] = var

print(tovapor)
print(min(tovapor.values()), max(tovapor.values()))
print(rayhash)
tovapors = sorted(tovapor.keys(), key=lambda i : rayhash[i])
tovapors = sorted(tovapors, key=lambda i : tovapor[i])
print(tovapors)
print(len(tovapors))
index = 0
shot = {}
while True:
    prev = -1
    for i in tovapors:
        if tovapor[i] == prev:
            continue
        if i in shot:
            continue
        shot[i] = 1
        index += 1
        if index % 10 == 0:
            print(index, i)
        prev = tovapor[i]
    if index > 200:
        break
