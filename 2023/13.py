import os, sys

LENGTH = 1419

f = open(os.path.join(sys.path[0], "13.txt"), "r")

def turnMatrix(matrix):
    foo = []
    for i in range(len(matrix[0])):
        rowfoo = []
        for j in range(len(matrix)):
            rowfoo.insert(0, matrix[j][i])
        foo.append(rowfoo)
    return foo

def printMatrix(matrix):
    for i in matrix:
        print("".join(i))
    print("")

matrixes = []
curmat = []
for i in range(LENGTH + 1):
    l = f.readline().strip()
    if l == "":
        matrixes.append(curmat)
        curmat = []
        continue
    curmat.append(list(l))

s = 0
for matrix in matrixes:
    m = matrix
    for t in range(2):
        begin = 0
        for y in range(len(m) - 1):
            if m[y] == m[y + 1]:
                begin = y + 1
                pone = y
                ptwo = y + 1
                break
        mirrors = True
        while pone >= 0 and ptwo < len(m):
            if m[pone] != m[ptwo]:
                mirrors = False
                break
            pone -= 1
            ptwo += 1
        if mirrors == True:
            s += begin * 100 if t == 1 else begin
        else:
            m = turnMatrix(m)
print(s)