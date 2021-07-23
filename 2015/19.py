import re
import random
from collections import defaultdict

changes = defaultdict(lambda : [])

sumup = {}

indx = 0
funcj = ""
counter = 0
def changer(mo):
    global indx
    global counter
    global funcj
    # print(counter, indx, mo.group(1))
    if counter != indx:
        counter += 1
        return mo.group(1)
    else:
        counter += 1
        return funcj

def changerb(mo):
    global indx
    global counter
    global twochanges
    print("changer", counter, indx, mo.group(1))
    if counter != indx:
        counter += 1
        return mo.group(1)
    else:
        counter += 1
        return twochanges[mo.group(1)]

twochanges = {}
for i in range(43):
    mo = re.match(r"(.+) => (.+)", input())
    changes[mo.group(1)].append(mo.group(2))
    twochanges[mo.group(2)] = mo.group(1)
input()
chem = input()

for i in changes:
    for j in changes[i]:
        funcj = j
        prlength = re.findall(r"%s" %(i), chem)
        length = len(prlength)
        for k in range(length):
            counter = 0
            indx = k
            copychem = re.sub(r"(%s)" %(i), changer, chem)
            # print(i, j, k, copychem)
            sumup[copychem] = 1
print(len(sumup))

que = [(chem, 0)]
lvl = 0

ctr = 0
thing = "(" + "|".join(twochanges.keys()) + ")"
while True:
    prechem = que.pop(0)
    lvl = prechem[1]
    print(lvl, len(prechem[0]), len(que), ctr, prechem[0])
    if prechem[0] == "e":
        print(prechem[1])
        exit(0)
    prlength = re.findall(r"%s" % (thing), prechem[0])
    length = len(prlength)
    if length == 0:
        exit(5)
    # for k in range(length):
    k = random.randint(0, length - 1)
    print(k, length, thing)
    counter = 0
    indx = k
    copychem = re.sub(r"%s" % (thing), changerb, prechem[0])
    # print(i, j, k, copychem)
    que.append((copychem, lvl + 1))
    ctr += 1


