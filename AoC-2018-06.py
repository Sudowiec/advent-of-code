from collections import defaultdict
coords = []
side = 360
border = 10000
counter = defaultdict(lambda: 0)
while True:
    try:
        inp = input()
    except EOFError:
        break
    coords.append(list(map(int, inp.split(", "))))
print(coords)
finites = list(range(len(coords)))

matrix = [["#" for i in range(side)] for j in range(side)]
for i in coords:
    matrix[i[1]][i[0]] = coords.index(i)

for y in range(side):
    for x in range(side):
        min_coord = -1
        smol_distance = 99999
        for i in coords:
            dist = abs(i[0] - x) + abs(i[1] - y)
            if dist == smol_distance:
                min_coord = "."
            elif dist < smol_distance:
                min_coord = coords.index(i)
                smol_distance = dist
        matrix[y][x] = min_coord
        counter[min_coord] += 1
del counter['.']

for i in range(side):
    if matrix[0][i] in counter:
        counter[matrix[0][i]] = -1
for i in range(side):
    if matrix[side - 1][i] in counter:
        counter[matrix[side - 1][i]] = -1
for i in range(side):
    if matrix[i][0] in counter:
        counter[matrix[i][0]] = -1
for i in range(side):
    if matrix[i][side - 1] in counter:
        counter[matrix[i][side - 1]] = -1

maxval = 0
for i in counter:
    if counter[i] > maxval:
        maxval = counter[i]
print(maxval)

valid_points = 0
for y in range(side):
    for x in range(side):
        sum_of_dist = 0
        for i in coords:
            sum_of_dist += abs(i[0] - x) + abs(i[1] - y)
            if sum_of_dist >= border:
                break
        if sum_of_dist < border:
            valid_points += 1
print(valid_points)