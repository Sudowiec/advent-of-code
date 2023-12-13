import os, sys

LENGTH = 140
EMPTYSIZE = 1000000

def turnMatrix(matrix):
    foo = []
    for x in range(len(matrix[0])):
        l = []
        for y in range(len(matrix)):
            l.append(matrix[y][x])
        foo.append(l)
    return foo

space = []
f = open(os.path.join(sys.path[0], "11.txt"), "r")

emptyRows = []
for i in range(LENGTH):
    line = list(f.readline().strip())
    if list(set(line)) == ["."]:
        emptyRows.append(i)
    space.append(line)

turned = turnMatrix(space)
emptyCols = []
for i in range(len(turned)):
    if list(set(turned[i])) == ["."]:
        emptyCols.append(i)
space = turnMatrix(turned)

print(emptyCols, emptyRows)


galaxies = []
for y in range(len(space)):
    for x in range(len(space[y])):
        if space[y][x] == "#":
            galaxies.append(str(x) + "," + str(y))
paths = {}
for i in galaxies:
    for j in galaxies:
        if i == j or (i + "|" + j) in paths or (j + "|" + i) in paths:
            continue
        ax = int(i.split(",")[0])
        bx = int(j.split(",")[0])
        ay = int(i.split(",")[1])
        by = int(j.split(",")[1])

        toMul = 0
        for r in emptyRows:
            if (r > ay and r < by) or (r > by and r < ay):
                toMul += 1
        for c in emptyCols:
            if (c > ax and c < bx) or (c > bx and c < ax):
                toMul += 1
        dist = abs(ax - bx) + abs(ay - by) + toMul * (EMPTYSIZE - 1)
        paths[i + "|" + j] = dist
print(sum(paths.values()))