# (abs() + abs() + abs()) / 2
x = 0
y = 0
z = 0
furth_dist = 0
inp = input().split(",")
for i in inp:
    if i == "n":
        y += 1
        z -= 1
    elif i == "ne":
        x += 1
        z -= 1
    elif i == "se":
        x += 1
        y -= 1
    elif i == "s":
        z += 1
        y -= 1
    elif i == "sw":
        z += 1
        x -= 1
    elif i == "nw":
        y += 1
        x -= 1
    dist = int((abs(x) + abs(y) + abs(z)) / 2)
    if dist > furth_dist:
        furth_dist = dist
findist = int((abs(x) + abs(y) + abs(z)) / 2)
print(furth_dist, findist)