import re
import copy
from collections import defaultdict
instructions = []

while True:
    try:
        inp = input()
    except EOFError:
        break

    builtins = []
    char = []
    for i in range(len(inp)):
        if inp[i] == "e" or inp[i] == "w":
            char.append(inp[i])
            builtins.append("".join(char))
            char = []
            continue
        char.append(inp[i])
    comains = builtins
    # comains = ",".join(comains)
    # for i in range(10):
    #     comains = re.sub(r"(^|,)w,(.+),e(,|$)", ",\\2,", comains)
    #     comains = re.sub(r"(^|,)e,(.+),w(,|$)", ",\\2,", comains)
    #     comains = re.sub(r"(^|,)se,(.+),nw(,|$)", ",\\2,", comains)
    #     comains = re.sub(r"(^|,)nw,(.+),se(,|$)", ",\\2,", comains)
    #     comains = re.sub(r"(^|,)sw,(.+),ne(,|$)", ",\\2,", comains)
    #     comains = re.sub(r"(^|,)ne,(.+),sw(,|$)", ",\\2,", comains)
    # comains = comains.split(",")
    # comains.pop()
    # comains.pop(0)
    # print(comains)
    instructions.append(comains)

tiles = defaultdict(lambda : "white")
lx = 0
mx = 0
ly = 0
my = 0
lz = 0
mz = 0
for insset in instructions:
    x = 0
    y = 0
    z = 0
    for i in insset:
        if i == "w":
            x -= 1
            y += 1
        elif i == "e":
            x += 1
            y -= 1
        elif i == "ne":
            x += 1
            z -= 1
        elif i == "nw":
            y += 1
            z -= 1
        elif i == "se":
            y -= 1
            z += 1
        elif i == "sw":
            z += 1
            x -= 1
    tile = str(z) + "," + str(y) + "," + str(x)
    if tiles[tile] == "white":
        tiles[tile] = "black"
    else:
        tiles[tile] = "white"
    lx = min(x, lx)
    mx = max(x, mx)
    ly = min(y, ly)
    my = max(y, my)
    lz = min(z, lz)
    mz = max(z, mz)
print(tiles)
count = 0
for i in tiles:
    if tiles[i] == "black":
        count += 1
print(count)
print(lx, mx, ly, my, lz, mz)

days = 100
rg = max(abs(mx - lx), abs(my - ly), abs(mz - lz))
mid = int((rg + 2 * days) / 2)
grid = [[["white" for x in range(rg + 2 * days)] for y in range(rg + 2 * days)] for z in range(rg + 2 * days)]
# print(grid)

for i in tiles:
    if tiles[i] == "white":
        continue
    coords = list(map(int, i.split(",")))
    print(coords)
    grid[coords[0] + mid][coords[1] + mid][coords[2] + mid] = "black"
# print(grid)

lx += mid
mx += mid
ly += mid
my += mid
lz += mid
mz += mid
for day in range(100):
    cogrid = copy.deepcopy(grid)
    count = 0
    for z in range(lz - 1, mz + 2):
        for y in range(ly - 1, my + 2):
            for x in range(lx - 1, mx + 2):
                if x + y + z - 3 * mid != 0:
                    continue
                curcol = grid[z][y][x]
                blacks = 0
                if grid[z][y+1][x-1] == "black":
                    blacks += 1
                if grid[z][y-1][x+1] == "black":
                    blacks += 1
                if grid[z-1][y][x+1] == "black":
                    blacks += 1
                if grid[z-1][y+1][x] == "black":
                    blacks += 1
                if grid[z+1][y-1][x] == "black":
                    blacks += 1
                if grid[z+1][y][x-1] == "black":
                    blacks += 1

                if curcol == "white" and blacks == 2:
                    cogrid[z][y][x] = "black"
                elif curcol == "black" and (blacks == 0 or blacks > 2):
                    cogrid[z][y][x] = "white"

                if cogrid[z][y][x] == "black":
                    count += 1
                    lx = min(x, lx)
                    mx = max(x, mx)
                    ly = min(y, ly)
                    my = max(y, my)
                    lz = min(z, lz)
                    mz = max(z, mz)

    print(day, count)
    grid = cogrid

    # for z in range(mid - rg - day, mid + rg + day):
    #     for y in range(mid - rg - day, mid + rg + day):
    #         for x in range(mid - rg - day, mid + rg + day):


