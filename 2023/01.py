import os, sys

def isNumber(inp):
    if inp in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        return True
    return False

s = 0
f = open(os.path.join(sys.path[0], "01.txt"), "r")
while True:
    l = f.readline().strip()
    if l == "":
        break
    for i in l:
        if isNumber(i):
            fs = i
            break
    for i in range(len(l) - 1, -1, -1):
        if isNumber(l[i]):
            sd = l[i]
            break
    s += int(fs + sd)
print(s)