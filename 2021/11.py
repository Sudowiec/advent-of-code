SIZE = 10
ITER = 100
octopuses = [["#" for i in range(12)]]
while True:
    try:
        inp = list(map(int, list(input())))
    except EOFError:
        break
    inp.insert(0, "#")
    inp.append("#")
    octopuses.append(inp)
octopuses.append(["#" for i in range(12)])
print(octopuses)

flashcount = 0
index = 0
while True:
    queue = []
    for y in range(1, SIZE + 1):
        for x in range(1, SIZE + 1):
            queue.append([y, x])

    while len(queue) > 0:
        q = queue.pop(0)
        y = q[0]
        x = q[1]
        if octopuses[y][x] == "#" or octopuses[y][x] == 10:
            continue
        octopuses[y][x] += 1
        if octopuses[y][x] == 10:
            flashcount += 1
            queue.extend([
                [y - 1, x],
                [y - 1, x + 1],
                [y, x + 1],
                [y + 1, x + 1],
                [y + 1, x],
                [y + 1, x - 1],
                [y, x - 1],
                [y - 1, x - 1]
            ])
    all = True
    for y in range(1, SIZE + 1):
        for x in range(1, SIZE + 1):
            if octopuses[y][x] == 10:
                octopuses[y][x] = 0
            else:
                all = False
    if all:
        break
    for i in octopuses:
        print("".join(map(str, i)))
    print()
    index += 1
print(index + 1)

