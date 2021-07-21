import math
import copy
from collections import defaultdict
photos = {}
id = 0
pic = []
a = 0

def photer(photos):
    right = []
    left = []
    up = []
    uppr = []
    down = []
    downpr = []
    for j in range(len(photos)):
        if j == 0:
            up = photos[j]
            uppr = reversed(photos[j])
            left.append(photos[j][0])
            right.append(photos[j][len(photos[j]) - 1])
        elif j == len(photos[j]) - 1:
            down = photos[j]
            downpr = reversed(photos[j])
            left.append(photos[j][0])
            right.append(photos[j][len(photos[j]) - 1])
        else:
            left.append(photos[j][0])
            right.append(photos[j][len(photos[j]) - 1])
    rightpr = int("".join(right), 2)
    right = int("".join(reversed(right)), 2)
    leftpr = int("".join(left), 2)
    left = int("".join(reversed(left)), 2)
    up = int("".join(up), 2)
    uppr = int("".join(uppr), 2)
    down = int("".join(down), 2)
    downpr = int("".join(downpr), 2)
    toret = {"right" : right, "left" : left, "up" : up, "down" : down, "rightpr" : rightpr, "leftpr" : leftpr, "uppr" : uppr, "downpr" : downpr}
    return toret

while True:
    try:
        inp = input()
    except EOFError:
        photos[id] = pic
        pic = []
        break


    if inp == "":
        photos[id] = pic
        pic = []
    elif inp[0] == "T":
        id = int(inp[5:9])
        a += 1
    else:
        inpl = list(inp)
        newinp = []
        N = len(inp)
        for i in inpl:
            if i == "#":
                newinp.append("1")
            else:
                newinp.append("0")
        pic.append(newinp)

a = int(math.sqrt(a))
finalmatrix = [["." for i in range(a)]for i in range(a)]

print(photos)
newphotos = {}
counter = defaultdict(lambda : 0)
for i in photos:
    newphotos[i] = photer(photos[i])
    for v in newphotos[i].values():
        counter[v] += 1

for i in newphotos:
    print(i, newphotos[i])
print(counter)

countervals = defaultdict(lambda : 0)
for i in counter.values():
    countervals[i] += 1
print(countervals)

corner = []
res = 1
for i in newphotos:
    count = 0
    for j in newphotos[i].values():
        count += counter[j]
    if count == 12:
        corner.append(i)
        res *= i
print(corner, res)

def rotate(matrix, times):
    newmatrix = copy.deepcopy(matrix)
    a = len(matrix) - 1
    for i in range(times):
        for y in range(len(matrix)):
            for x in range(len(matrix)):
                newx = a - y
                newy = x
                newmatrix[newy][newx] = matrix[y][x]
        matrix = copy.deepcopy(newmatrix)
    return matrix

def flip(matrix, parameter):
    newmatrix = copy.deepcopy(matrix)
    a = len(matrix) - 1
    if parameter == "y":
        for y in range(len(matrix)):
            for x in range(len(matrix)):
                newx = a - x
                newmatrix[y][newx] = matrix[y][x]
        matrix = copy.deepcopy(newmatrix)
    elif parameter == "x":
        for y in range(len(matrix)):
            for x in range(len(matrix)):
                newy = a - y
                newmatrix[newy][x] = matrix[y][x]
        matrix = copy.deepcopy(newmatrix)
    else:
        exit(5)
    return matrix

def printmat(matrix):
    for i in matrix:
        print(" ".join(list(map(str, i))))
    print()

firstid = corner[0]
finalmatrix[0][0] = firstid
print(newphotos[firstid])
while True:
    if counter[newphotos[firstid]["right"]] == 2 and counter[newphotos[firstid]["down"]] == 2 and counter[newphotos[firstid]["left"]] == 1 and counter[newphotos[firstid]["up"]] == 1:
        break
    photos[firstid] = rotate(photos[firstid], 1)
    newphotos[firstid] = photer(photos[firstid])
used = {firstid : True}

for num in range(1, a):
    lastright = newphotos[finalmatrix[0][num - 1]]["right"] # {'right': 498, 'left': 841, 'up': 710, 'down': 564, 'rightpr': 318, 'leftpr': 587, 'uppr': 397, 'downpr': 177}
    for id in newphotos:
        if id in used:
            continue
        if lastright in newphotos[id].values():
            if newphotos[id]["left"] == lastright:
                used[id] = True
                finalmatrix[0][num] = id
                break
            elif newphotos[id]["right"] == lastright:
                photos[id] = flip(photos[id], "y")
                newphotos[id] = photer(photos[id])
                used[id] = True
                finalmatrix[0][num] = id
                break
            elif newphotos[id]["up"] == lastright:
                photos[id] = rotate(photos[id], 3)
                newphotos[id] = photer(photos[id])
                used[id] = True
                finalmatrix[0][num] = id
                break
            elif newphotos[id]["down"] == lastright:
                photos[id] = flip(photos[id], "x")
                photos[id] = rotate(photos[id], 3)
                newphotos[id] = photer(photos[id])
                used[id] = True
                finalmatrix[0][num] = id
                break
            elif newphotos[id]["rightpr"] == lastright:
                photos[id] = rotate(photos[id], 2)
                newphotos[id] = photer(photos[id])
                used[id] = True
                finalmatrix[0][num] = id
                break
            elif newphotos[id]["leftpr"] == lastright:
                photos[id] = flip(photos[id], "x")
                newphotos[id] = photer(photos[id])
                used[id] = True
                finalmatrix[0][num] = id
                break
            elif newphotos[id]["uppr"] == lastright:
                photos[id] = flip(photos[id], "x")
                photos[id] = rotate(photos[id], 1)
                newphotos[id] = photer(photos[id])
                used[id] = True
                finalmatrix[0][num] = id
                break
            elif newphotos[id]["downpr"] == lastright:
                photos[id] = rotate(photos[id], 1)
                newphotos[id] = photer(photos[id])
                used[id] = True
                finalmatrix[0][num] = id
                break
            else:
                exit(6)

for mainx in range(a):
    for mainy in range(1, a):
        lastdown = newphotos[finalmatrix[mainy - 1][mainx]]["down"]
        for id in newphotos:
            if id in used:
                continue
            if lastdown in newphotos[id].values():
                if newphotos[id]["up"] == lastdown:
                    used[id] = True
                    finalmatrix[mainy][mainx] = id
                    break
                elif newphotos[id]["right"] == lastdown:
                    photos[id] = flip(photos[id], "y")
                    photos[id] = rotate(photos[id], 1)
                    newphotos[id] = photer(photos[id])
                    used[id] = True
                    finalmatrix[mainy][mainx] = id
                    break
                elif newphotos[id]["down"] == lastdown:
                    photos[id] = flip(photos[id], "x")
                    newphotos[id] = photer(photos[id])
                    used[id] = True
                    finalmatrix[mainy][mainx] = id
                    break
                elif newphotos[id]["left"] == lastdown:
                    photos[id] = rotate(photos[id], 1)
                    newphotos[id] = photer(photos[id])
                    used[id] = True
                    finalmatrix[mainy][mainx] = id
                    break
                elif newphotos[id]["rightpr"] == lastdown:
                    photos[id] = rotate(photos[id], 3)
                    newphotos[id] = photer(photos[id])
                    used[id] = True
                    finalmatrix[mainy][mainx] = id
                    break
                elif newphotos[id]["leftpr"] == lastdown:
                    photos[id] = rotate(photos[id], 1)
                    photos[id] = flip(photos[id], "y")
                    newphotos[id] = photer(photos[id])
                    used[id] = True
                    finalmatrix[mainy][mainx] = id
                    break
                elif newphotos[id]["uppr"] == lastdown:
                    photos[id] = flip(photos[id], "y")
                    newphotos[id] = photer(photos[id])
                    used[id] = True
                    finalmatrix[mainy][mainx] = id
                    break
                elif newphotos[id]["downpr"] == lastdown:
                    photos[id] = rotate(photos[id], 2)
                    newphotos[id] = photer(photos[id])
                    used[id] = True
                    finalmatrix[mainy][mainx] = id
                    break
                else:
                    exit(6)

printmat(finalmatrix)
for y in range(a):
    for k in range(N):
        for x in range(a):
            print("".join(photos[finalmatrix[y][x]][k]) + " ", end="")
        print()
    print()
B = (N - 2) * a
finalphoto = [[] for i in range(B)]

w = 0
for y in range(a):
    for k in range(1, N - 1):
        for x in range(a):
            row = photos[finalmatrix[y][x]][k]
            row.pop()
            row.pop(0)
            finalphoto[w] += row
        w += 1

printmat(finalphoto)

monstertxt = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]
monster = [["." for i in range(len(monstertxt[0]))] for i in range(len(monstertxt))]
for i in range(len(monstertxt)):
    for j in range(len(monstertxt[i])):
        if monstertxt[i][j] == " ":
            monster[i][j] = '0'
        else:
            monster[i][j] = '1'
printmat(monster)

rotphotos = [finalphoto, rotate(finalphoto, 1), rotate(finalphoto, 2), rotate(finalphoto, 3), flip(finalphoto, "x"), rotate(flip(finalphoto, "x"), 1), rotate(flip(finalphoto, "x"), 2), rotate(flip(finalphoto, "x"), 3)]

monsterscount = 0
for pic in rotphotos:
    for y in range(len(pic) - len(monster)):
        for x in range(len(pic[0]) - len(monster[0])):
            ismonster = True
            for mony in range(len(monster)):
                for monx in range(len(monster[0])):
                    if monster[mony][monx] == '1':
                        if pic[y + mony][x + monx] != '1':
                            ismonster = False
                            break
            if ismonster:
                monsterscount += 1
print(monsterscount)

def onecounter(cut):
    number = 0
    for i in cut:
        for j in i:
            if j == "1":
                number += 1
    return number

print(onecounter(finalphoto) - monsterscount * onecounter(monster))




