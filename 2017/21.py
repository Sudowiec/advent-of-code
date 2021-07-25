THRESHOLD = 1
ITERATIONS = 5

def checkSize(tile):
    tp = tile.split("/")
    return len(tp[0])

def printTile(tile):
    tp = tile.split("/")
    for i in tp:
        print(i)

def flipTile(tile, flip):
    sidelen = checkSize(tile)
    rttile = []
    for i in range(sidelen):
        rttile.append(list("-" for j in range(sidelen)))

    if flip == "lr":
        for i in range(sidelen):
            rttile[i] = tp[i][::-1]
    elif flip == "ud":
        for i in range(sidelen):
            rttile[i] = tp[sidelen - i - 1]

    return "/".join(rttile)

def rotateTile(tile):
    sidelen = checkSize(tile)
    rttile = []
    for i in range(sidelen):
        rttile.append(list("-" for j in range(sidelen)))

    for i in range(sidelen):
        for j in range(sidelen):
            rttile[j][sidelen - i - 1] = list(tp[i])[j]

    for i in range(sidelen):
        rttile[i] = "".join(rttile[i])
    return "/".join(rttile)

tile = ".#.#/..##/####/.#.#"
printTile(tile)

rules23 = {}
rules34 = {}
indx = 0
while True:
    try:
        inp = input().split(" => ")
    except EOFError:
        break
    if indx < THRESHOLD:
        rules23[inp[0]] = inp[1]
    else:
        rules34[inp[0]] = inp[1]
    indx += 1

for iter in range(ITERATIONS):
    size = checkSize(tile)
    if size % 2 == 0:
        difer = 2
