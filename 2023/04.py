import os, sys

f = open(os.path.join(sys.path[0], "04.txt"), "r")

LENGTH = 193

stack = []
idcount = {}

for i in range(LENGTH):
    inp = f.readline().strip()[7:].split("|")
    first = list(filter(("").__ne__, inp[0].split(" ")))
    second = list(filter(("").__ne__, inp[1].split(" ")))
    stack.append({i: [first, second]})
    idcount[i] = 1

for cur in stack:
    curid = list(cur.keys())[0]
    res = len(set(cur[curid][0]) & set(cur[curid][1]))
    inc = idcount[curid]
    for i in range(res):
        idcount[curid + i + 1] += inc
    print(idcount)
    
s = 0

for i in idcount:
    s += idcount[i] 

print(s)