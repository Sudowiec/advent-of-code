import copy
import time
import os
import hashlib
clear = lambda: os.system('cls')
matrix = []
side = 50
matrix_hash = {}
indx = 1
offset = 0
cycle_len = 0
while True:
    try:
        matrix.append(list(input()))
    except EOFError:
        break

for step in range(23 + 417):
    # clear()
    print(indx)
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

    # hash_func.update(bytes(str(new_matrix), "utf-8"))
    hash_func = hashlib.md5()
    hash_func.update(str(new_matrix).encode("ASCII"))
    key = hash_func.hexdigest()
    # print(key)
    # print(len(matrix_hash))
    if key in matrix_hash:
        offset = matrix_hash[key] - 1
        cycle_len = indx - matrix_hash[key]
        break
    else:
        matrix_hash[key] = indx
    matrix = copy.deepcopy(new_matrix)
    indx += 1
# looking_for = (1000000000 - offset) % cycle_len
# looking_for = (500 - offset) % cycle_len
# print(looking_for, cycle_len, offset)
# 187186

trees = 0
lumbs = 0
for i in matrix:
    for j in i:
        if j == "#":
            lumbs += 1
        elif j == "|":
            trees += 1
print(trees * lumbs)