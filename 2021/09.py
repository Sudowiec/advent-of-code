seafloor = []
while True:
    try:
        seafloor.append(list(map(int, list(input()))))
    except EOFError:
        break
height = len(seafloor)
width = len(seafloor[0])

# adding border
for i in seafloor:
    i.append(10)
    i.insert(0, 10)
seafloor.append([10 for i in range(width + 2)])
seafloor.insert(0, [10 for i in range(width + 2)])
print(seafloor)

# searching lowpoints
lowpoints = []
lowpoints_coords = []
for y in range(1, height + 1):
    for x in range(1, width + 1):
        num = seafloor[y][x]
        if num >= seafloor[y + 1][x]:
            continue
        if num >= seafloor[y - 1][x]:
            continue
        if num >= seafloor[y][x + 1]:
            continue
        if num >= seafloor[y][x - 1]:
            continue
        lowpoints.append(num + 1)
        lowpoints_coords.append(str(y) + "," + str(x))

# finding basins recursion
def basin(matrix, x, y):
    counter = 1
    num = matrix[y][x]
    bt.append([y, x])
    if num < matrix[y + 1][x] and matrix[y + 1][x] < 9 and [y+1, x] not in bt:
        counter += basin(matrix, x, y + 1)
    if num < matrix[y - 1][x] and matrix[y - 1][x] < 9 and [y-1, x] not in bt:
        counter += basin(matrix, x, y - 1)
    if num < matrix[y][x + 1] and matrix[y][x + 1] < 9 and [y, x+1] not in bt:
        counter += basin(matrix, x + 1, y)
    if num < matrix[y][x - 1] and matrix[y][x - 1] < 9 and [y, x-1] not in bt:
        counter += basin(matrix, x - 1, y)
    return counter

basins = []
global bt
bt = []
for i in lowpoints_coords:
    x = int(i.split(",")[1])
    y = int(i.split(",")[0])
    basins.append(basin(seafloor, x, y))
basins = sorted(basins)
print(basins)
mul = 1
for i in range(3):
    mul *= basins.pop()
print(mul)