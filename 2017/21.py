def printTile(tile):
    tp = tile.split("/")
    for i in tp:
        print(i)

def flipTile(tile, flip):
    tp = tile.split("/")
    sidelen = len(tp[0])
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
    sidelen = len(tp[0])
    rttile = []
    for i in range(sidelen):
        rttile.append(list("-" for j in range(sidelen)))

    for i in range(sidelen):
        for j in range(sidelen):
            rttile[j][sidelen - i - 1] = list(tp[i])[j]

    for i in range(sidelen):
        rttile[i] = "".join(rttile[i])
    return "/".join(rttile)



tile = ".#./..#/###"
printTile(tile)

