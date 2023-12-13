import os, sys

LENGTH = 140

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

for i in range(LENGTH):
    line = list(f.readline().strip())
    if list(set(line)) == ["."]:
        space.append(line)
    space.append(line)

turned = turnMatrix(space)
toDub = []
for i in range(len(turned)):
    if list(set(turned[i])) == ["."]:
        toDub.append(i)

for i in range(len(toDub)):
    turned.insert(toDub[i] + i, ["." for i in range(len(turned[0]))])
space = turnMatrix(turned)


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
        dist = abs(int(i.split(",")[0]) - int(j.split(",")[0])) + abs(int(i.split(",")[1]) - int(j.split(",")[1]))
        paths[i + "|" + j] = dist
print(sum(paths.values()))