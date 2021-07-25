import math
ITERATIONS = 5

def checkSize(tile):
    tp = tile.split("/")
    return len(tp[0])

def printTile(tile):
    tp = tile.split("/")
    for i in tp:
        print(i)

def flipTile(tile, flip):
    tp = tile.split("/")
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
    tp = tile.split("/")
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

def tileCode(tile):
    codedtile = []
    for i in tile:
        codedtile.append("".join(i))
    return "/".join(codedtile)

def tileDecode(tile):
    tile = tile.split("/")
    decodedtile = []
    for i in tile:
        decodedtile.append(list(i))
    return  decodedtile

def allPossibilities(tile):
    possibilities = [tile]
    possibilities.append(rotateTile(tile))
    possibilities.append(rotateTile(rotateTile(tile)))
    possibilities.append(rotateTile(rotateTile(rotateTile(tile))))
    possibilities.append(flipTile(tile, "lr"))
    possibilities.append(rotateTile(flipTile(tile, "lr")))
    possibilities.append(rotateTile(rotateTile(flipTile(tile, "lr"))))
    possibilities.append(rotateTile(rotateTile(rotateTile(flipTile(tile, "lr")))))
    return possibilities

tile = ".#./..#/###"
printTile(tile)

# rules initialization
rules = {}
indx = 0
while True:
    try:
        inp = input().split(" => ")
    except EOFError:
        break
    rules[inp[0]] = inp[1]
    indx += 1

# main loop
for iter in range(ITERATIONS):
    worktile = tileDecode(tile)
    size = checkSize(tile)
    division = 0

    # division by 2
    if size % 2 == 0:
        division = 2
        up = []
        down = []
        for i in range(len(worktile)):
            if i % 2 == 0:
                up.append(worktile[i])
            else:
                down.append(worktile[i])
        numoftiles = int(size / 2) ** 2
        up = sum(up, [])
        down = sum(down, [])
        smalltiles = []
        for i in range(numoftiles):
            part1 = []
            for j in range(2):
                part1.append(up.pop(0))
            part2 = []
            for j in range(2):
                part2.append(down.pop(0))
            smalltiles.append("".join(part1) + "/" + "".join(part2))

    # division by 3
    elif size % 3 == 0:
        division = 3
        up = []
        mid = []
        down = []
        for i in range(len(worktile)):
            if i % 3 == 0:
                up.append(worktile[i])
            elif i % 3 == 1:
                mid.append(worktile[i])
            else:
                down.append(worktile[i])
        numoftiles = int(size / 3) ** 2
        up = sum(up, [])
        mid = sum(mid, [])
        down = sum(down, [])
        smalltiles = []
        for i in range(numoftiles):
            part1 = []
            for j in range(3):
                part1.append(up.pop(0))
            part2 = []
            for j in range(3):
                part2.append(mid.pop(0))
            part3 = []
            for j in range(3):
                part3.append(down.pop(0))
            smalltiles.append("".join(part1) + "/" + "".join(part2) + "/" + "".join(part3))

    # changing tiles by the rules
    newtiles = []
    for subject in smalltiles:
        pos = allPossibilities(subject)
        for i in pos:
            if i in rules:
                newtiles.append(rules[i])
                break
    newtiles = "/".join(newtiles)
    if iter == 0:
        tile = newtiles
    else:
        newtiles = tileDecode(newtiles)
        switchtiles = []
        for i in range(len(newtiles[0]) * int(math.sqrt(numoftiles))):
            idk = []
            for j in range(int(math.sqrt(numoftiles))):
                idk += newtiles[i + j * (division + 1)]
            switchtiles.append(idk)
        switchtiles = tileCode(switchtiles)
        tile = switchtiles
    print()
    printTile(tile)

    count = 0
    for i in tile:
        if i == "#":
            count += 1
    print(count)
