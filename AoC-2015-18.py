import copy
import time
import os
clear = lambda: os.system('cls')
matrix = []
side = 50
while True:
    try:
        matrix.append(list(input()))
    except EOFError:
        break
for i in matrix:
    print("".join(i))

for step in range(10):
    # clear()
    new_matrix = copy.deepcopy(matrix)

    matrix.insert(0, [ "-" for i in range(side)])
    matrix.append([ "-" for i in range(side)])
    for i in matrix:
        i.insert(0, "-")
        i.append("-")

    for y in range(1, side + 1):
        for x in range(1, side + 1):
            objects = {"|" : 0, "#" : 0, "." : 0, "-" : 0}
            objects[matrix[y][x - 1]] += 1
            objects[matrix[y + 1][x - 1]] += 1
            objects[matrix[y + 1][x]] += 1
            objects[matrix[y + 1][x + 1]] += 1
            objects[matrix[y][x + 1]] += 1
            objects[matrix[y - 1][x + 1]] += 1
            objects[matrix[y - 1][x]] += 1
            objects[matrix[y - 1][x - 1]] += 1

            if matrix[y][x] == "." and objects["|"] >= 3:
                new_matrix[y - 1][x - 1] = "|"
            if matrix[y][x] == "|" and objects["#"] >= 3:
                new_matrix[y - 1][x - 1] = "#"
            if matrix[y][x] == "#" and (objects["#"] == 0 or objects["|"] == 0):
                new_matrix[y - 1][x - 1] = "."
    print("")
    for i in new_matrix:
        print("".join(i))
    print("")
    time.sleep(0.05)
    matrix = copy.deepcopy(new_matrix)
trees = 0
lumbs = 0
for i in matrix:
    for j in i:
        if j == "#":
            lumbs += 1
        elif j == "|":
            trees += 1
print(trees * lumbs)