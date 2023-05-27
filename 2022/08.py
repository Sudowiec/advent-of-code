DOPRINTGRID = False
def printgrid(grid, label = ""):
    if DOPRINTGRID:
        print(label)
        for i in grid:
            print("".join(list(map(str, i))))
        print("")

grid = []
inp = open("2022/08.txt", "r")
while True:
    line = list(map(int, list(inp.readline().strip())))
    if not line:
        break
    grid.append(line)
size = len(grid)

# PART 1
# right
rgrid = [["" for j in range(size)] for i in range(size)]
for i in range(size):
    top = grid[i][0]
    rgrid[i][0] = "0"
    for j in range(1, size):
        if grid[i][j] > top:
            top = grid[i][j]
            rgrid[i][j] = "0"
        else:
            rgrid[i][j] = "O"
printgrid(rgrid, "Right:")

# left
lgrid = [["" for j in range(size)] for i in range(size)]
for i in range(size-1, -1, -1):
    top = grid[i][size-1]
    lgrid[i][size-1] = "0"
    for j in range(size-2, -1, -1):
        if grid[i][j] > top:
            top = grid[i][j]
            lgrid[i][j] = "0"
        else:
            lgrid[i][j] = "O"
printgrid(lgrid, "Left:")

# top
tgrid = [["" for j in range(size)] for i in range(size)]
for i in range(size):
    top = grid[0][i]
    tgrid[0][i] = "0"
    for j in range(1, size):
        if grid[j][i] > top:
            top = grid[j][i]
            tgrid[j][i] = "0"
        else:
            tgrid[j][i] = "O"
printgrid(tgrid, "Top:")

# bottom
bgrid = [["" for j in range(size)] for i in range(size)]
for i in range(size-1, -1, -1):
    top = grid[size-1][i]
    bgrid[size-1][i] = "0"
    for j in range(size-2, -1, -1):
        if grid[j][i] > top:
            top = grid[j][i]
            bgrid[j][i] = "0"
        else:
            bgrid[j][i] = "O"
printgrid(bgrid, "Bottom:")

# main
s = 0
mgrid = [["O" for j in range(size)] for i in range(size)]
for i in range(size):
    for j in range(size):
        if rgrid[i][j] == '0' or lgrid[i][j] == '0' or tgrid[i][j] == '0' or bgrid[i][j] == '0':
            mgrid[i][j] = '0'
            s += 1
printgrid(mgrid, "Whole:")
print("Visible trees:", s)

# PART 2
size += 2
grid.insert(0, ["X" for i in range(size)])
grid.append(["X" for i in range(size)])
for i in range(1, size - 1):
    grid[i].insert(0, "X")
    grid[i].append("X")
printgrid(grid)

scores = []
for y in range(1, size - 1):
    for x in range(1, size - 1):
        height = grid[y][x]
        
        # top
        i = 0
        t = 0
        while True:
            i += 1
            curheight = grid[y - i][x]
            if curheight == "X":
                break
            t += 1
            if curheight >= height:
                break

        # bottom
        i = 0
        b = 0
        while True:
            i += 1
            curheight = grid[y + i][x]
            if curheight == "X":
                break
            b += 1
            if curheight >= height:
                break

        # right
        i = 0
        r = 0
        while True:
            i += 1
            curheight = grid[y][x + i]
            if curheight == "X":
                break
            r += 1
            if curheight >= height:
                break

        # left
        i = 0
        l = 0
        while True:
            i += 1
            curheight = grid[y][x - i]
            if curheight == "X":
                break
            l += 1
            if curheight >= height:
                break

        # count
        scores.append(l * r * t * b)
print("Highest score:", max(scores))