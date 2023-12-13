import os, sys

LENGTH = 1000

f = open(os.path.join(sys.path[0], "12.txt"), "r")

def isValid(row, log):
    r = list(filter(("").__ne__, row.split(".")))
    if len(r) != len(log):
        return False
    for i in range(len(r)):
        if len(r[i]) != log[i]:
            return False
    return True

def fillQuestions(row, number, addz):
    b = str(bin(number))[2:]
    b = b.replace("0", ".")
    b = b.replace("1", "#")
    while len(b) < addz:
        b = "." + b

    ind = 0
    for i in range(len(row)):
        if row[i] == "?":
            row = row[:i] + b[ind] + row[i + 1:]
            ind += 1
    
    return row

s = 0
for i in range(LENGTH):
    print(i)
    l = f.readline().strip().split(" ")
    springRow = l[0]*5
    springLog = list(map(int, l[1].split(",")))
    
    qs = springRow.count("?")
    numOfPos = pow(2, qs)
    for j in range(numOfPos):
        t = fillQuestions(springRow, j, qs)
        if isValid(t, springLog):
            s += 1
print(s)