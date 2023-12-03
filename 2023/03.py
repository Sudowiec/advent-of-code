import os, sys

NUMS = "0123456789"
LENGTH = 140

matrix = []

def getNumber(turn, x, y):
    px = x
    num = ""
    if turn == "left":
        while matrix[y][px] != ".":
            num = matrix[y][px] + num
            px -= 1
    elif turn == "right":
        while matrix[y][px] != ".":
            num += matrix[y][px]
            px += 1
    elif turn == "both":
        while matrix[y][px] != ".":
            num = matrix[y][px] + num
            px -= 1
        px = x + 1
        while matrix[y][px] != ".":
            num += matrix[y][px]
            px += 1
    return int(num)

f = open(os.path.join(sys.path[0], "03.txt"), "r")

for i in range(LENGTH):
    matrix.append(["."] + list(f.readline().strip()) + ["."])
matrix.append(["." for i in range(len(matrix[0]))])
matrix.insert(0, ["." for i in range(len(matrix[0]))])

for i in matrix:
    print("".join(i))

s = 0
for y in range(len(matrix)):
    for x in range(len(matrix[0])):
        if matrix[y][x] != "*":
            continue
        
        ratio = 1
        amountOfNums = 0

        if matrix[y][x - 1] in NUMS: # LEFT
            ratio *= getNumber("left", x - 1, y)
            amountOfNums += 1
        if matrix[y][x + 1] in NUMS: # RIGHT
            ratio *= getNumber("right", x + 1, y)
            amountOfNums += 1

        if matrix[y - 1][x] in NUMS: # UP
            ratio *= getNumber("both", x, y - 1)
            amountOfNums += 1
        else:
            if matrix[y - 1][x - 1] in NUMS: # UP LEFT
                ratio *= getNumber("left", x - 1, y - 1)
                amountOfNums += 1
            if matrix[y - 1][x + 1] in NUMS: # UP RIGHT
                ratio *= getNumber("right", x + 1, y - 1)
                amountOfNums += 1
        
        if matrix[y + 1][x] in NUMS: # DOWN
            ratio *= getNumber("both", x, y + 1)
            amountOfNums += 1
        else:
            if matrix[y + 1][x - 1] in NUMS: # DOWN LEFT
                ratio *= getNumber("left", x - 1, y + 1)
                amountOfNums += 1
            if matrix[y + 1][x + 1] in NUMS: # DOWN RIGHT
                ratio *= getNumber("right", x + 1, y + 1)
                amountOfNums += 1
        
        if amountOfNums == 2:
            s += ratio
print(s)                