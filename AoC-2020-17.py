import copy
a = 8
rounds = 6
margin = rounds + 1
prevoid = [[[["." for i in range(a + 2 * margin)] for i in range(a + 2 * margin)] for i in range(a + 2 * margin)] for i in range(a + 2 * margin)]


indx = 0
while True:
    try:
        inp = input()
    except EOFError:
        break

    inp = list(inp)
    for i in range(len(inp)):
        if inp[i] == "#":
            prevoid[int(a / 2) + margin][int(a / 2) + margin][indx + margin][i + margin] = "#"
    indx += 1
print(prevoid)

full_amount = 0
for cycle in range(rounds):
    void = copy.deepcopy(prevoid)
    for w in range(len(void)):
        for z in range(len(void)):
            for y in range(len(void)):
                for x in range(len(void)):
                    state = void[w][z][y][x]
                    neighbours = 0
                    for ww in range(-1, 2):
                        for zz in range(-1, 2):
                            for yy in range(-1, 2):
                                for xx in range(-1, 2):
                                    if ww == 0 and xx == 0 and yy == 0 and zz == 0:
                                        continue
                                    try:
                                        if void[w + ww][z + zz][y + yy][x + xx] == "#":
                                            neighbours += 1
                                    except IndexError:
                                        continue

                    if state == "#":
                        if neighbours == 2 or neighbours == 3:
                            prevoid[w][z][y][x] = "#"
                        else:
                            prevoid[w][z][y][x] = "."
                    elif state == ".":
                        if neighbours == 3:
                            prevoid[w][z][y][x] = "#"
                        else:
                            prevoid[w][z][y][x] = "."

    amount = 0
    for i in prevoid:
        for j in i:
            for k in j:
                for l in k:
                    if l == "#":
                        amount += 1
    # print(prevoid)
    print(amount)




