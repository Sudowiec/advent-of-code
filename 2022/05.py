from collections import defaultdict
import re

# get crates state
inps = []
while True:
    inp = input()
    if inp == "":
        break
    inps.append(inp)
numOfSlots =int(inps[len(inps) - 1][-2])
inps.pop()

crates = defaultdict(lambda : [])
indx = 1
for i in range(numOfSlots):
    for j in inps:
        if j[indx] != " ":
            crates[i + 1].insert(0, j[indx])
    indx += 4

# rearrange crates
while True:
    try:
        inp = input()
    except EOFError:
        break
    reInp = [int(s) for s in re.findall(r'\d+', inp)]
    toMove = crates[reInp[1]][len(crates[reInp[1]]) - reInp[0]:]
    for i in range(reInp[0]):
        crates[reInp[1]].pop()
    crates[reInp[2]].extend(toMove)

finStr = ""
for i in range(1, numOfSlots + 1):
    finStr += crates[i].pop()
print(finStr)