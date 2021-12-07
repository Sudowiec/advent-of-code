import copy
ITERATIONS = 5
# init
grid = "010001111"
size = 3
rules = {}
while True:
    try:
        inp = input().split(" => ")
        one = "".join(inp[0].split("/"))
        one = one.replace(".", "0")
        one = one.replace("#", "1")
        two = "".join(inp[1].split("/"))
        two = two.replace(".", "0")
        two = two.replace("#", "1")
        rules[one] = two
    except EOFError:
        break

def printgrid(grid, size):
    for i in range(size - 1, size**2, size):
        tp = grid[i-size + 1:i + 1]
        tp = tp.replace("0", ".")
        tp = tp.replace("1", "#")
        print(tp)


def comparator(grid, pattern, size):
    opgrid = copy.deepcopy(grid)
    for it in range(4):
        # rotate
        new = ["" for i in range(size**2)]
        indx = 0
        for i in range(size - 1, -1, -1):
            for j in range(size):
                new[i + j * size] = opgrid[indx]
                indx += 1
        opgrid = "".join(new)
        if opgrid == pattern:
            return True
        # flip
        indx = 0
        new = ["" for i in range(size ** 2)]
        for i in range(size - 1, -1, -1):
            for j in range(size):
                new[i * size + j] = opgrid[indx]
                indx += 1
        if "".join(new) == pattern:
            return True

# first rebuild
printgrid(grid, size)
for i in rules:
    if comparator(grid, i, size):
        grid = rules[i]
        size += 1
        break
printgrid(grid, size)

# main loop
for index in range(ITERATIONS - 1):

    if size % 2 == 0:
        division = 2
    else:
        division = 3
    numofrows = size // division
    tiles = []

    if division == 2:
        for i in range(numofrows):
            beg = 2 * i * size
            upper = grid[beg : beg + size]
            downer = grid[beg + size : beg + 2 * size]
            print(upper)
            print(downer)
            for j in range(2, size + 1, 2):
                tiles.append(upper[j - 2 : j] + downer[j - 2: j])
        print(tiles)
        for j in range(len(tiles)):
            for i in rules:
                if comparator(tiles[j], i, 2):
                    tiles[j] = rules[i]
                    break
        size += numofrows
        print(tiles)

        grid = ""
        for i in range(0, numofrows**2, numofrows):
            upper = ""
            mid = ""
            downer = ""
            for j in range(numofrows):
                upper += tiles[i + j][0:3]
            for j in range(numofrows):
                mid += tiles[i + j][3:6]
            for j in range(numofrows):
                downer += tiles[i + j][6:9]
            grid += upper + mid + downer

    if division == 3:
        for i in range(numofrows):
            beg = 3 * i * size
            upper = grid[beg : beg + size]
            mid = grid[beg + size : beg + 2 * size]
            downer = grid[beg + 2 * size : beg + 3 * size]
            print(upper)
            print(mid)
            print(downer)
            for j in range(3, size + 1, 3):
                tiles.append(upper[j - 3 : j] + mid[j - 3 : j] + downer[j - 3 : j])
        print(tiles)
        for j in range(len(tiles)):
            for i in rules:
                if comparator(tiles[j], i, 3):
                    tiles[j] = rules[i]
                    break
        size += numofrows
        print(tiles)

        grid = ""
        for i in range(0, numofrows**2, 3):
            upper = ""
            midone = ""
            midtwo = ""
            downer = ""
            for j in range(numofrows):
                upper += tiles[i + j][0:4]
            for j in range(numofrows):
                midone += tiles[i + j][4:8]
            for j in range(numofrows):
                midtwo += tiles[i + j][8:12]
            for j in range(numofrows):
                downer += tiles[i + j][12:16]
            grid += upper + midone + midtwo + downer
    print(grid)
    printgrid(grid, size)
print(grid.count("1"))


