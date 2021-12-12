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

