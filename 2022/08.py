def printgrid(grid):
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
print("Right:")
printgrid(rgrid)

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
print("Left:")
printgrid(lgrid)

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
print("Top:")
printgrid(tgrid)

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
print("Bottom:")
printgrid(bgrid)

# main
s = 0
mgrid = [["O" for j in range(size)] for i in range(size)]
for i in range(size):
    for j in range(size):
        if rgrid[i][j] == '0' or lgrid[i][j] == '0' or tgrid[i][j] == '0' or bgrid[i][j] == '0':
            mgrid[i][j] = '0'
            s += 1
print("Whole:")
printgrid(mgrid)
print("Visible trees:", s)