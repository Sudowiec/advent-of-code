import os, sys

LENGTH = 100
RED = 12
GREEN = 13
BLUE = 14

f = open(os.path.join(sys.path[0], "02.txt"), "r")
s = 0

for i in range(LENGTH):
    gId = i + 1
    confs = f.readline().strip().split(": ")[1].split("; ")
    maind = {"red" : 0, "green" : 0, "blue" : 0}
    for j in range(len(confs)):
        d = {"red" : 0, "green" : 0, "blue" : 0}
        colors = confs[j].split(", ")     
        for k in colors:
            d[k.split(" ")[1]] += int(k.split(" ")[0])
        for k in d:
            if d[k] > maind[k]:
                maind[k] = d[k]
    print(maind)
    p = 1
    for j in maind:
        p *= maind[j]
    s += p
print(s)