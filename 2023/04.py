import os, sys

f = open(os.path.join(sys.path[0], "04.txt"), "r")

LENGTH = 193

s = 0

for i in range(LENGTH):
    inp = f.readline().strip()[7:].split("|")
    first = list(filter(("").__ne__, inp[0].split(" ")))
    second = list(filter(("").__ne__, inp[1].split(" ")))
    res = 2**(len(set(first) & set(second)) - 1)
    if res != 0.5:
        s += res

print(s)