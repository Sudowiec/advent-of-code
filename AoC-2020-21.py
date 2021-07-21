import re
from collections import defaultdict

ingrhash = defaultdict(lambda : [])
alghash = defaultdict(lambda : [])
foods = []
numalg = defaultdict(lambda : 0)
finuming = defaultdict(lambda : 0)
finalingr = {}
finalalg = {}
while True:
    try:
        inp = input()
    except EOFError:
        break
    mo = re.findall(r"(.+) \(contains (.+)\)", inp)
    ingr = mo[0][0].split(" ")
    alg = mo[0][1].split(", ")
    print(ingr, alg)
    foods.append((ingr, alg))
    for i in ingr:
        ingrhash[i] += alg
        finuming[i] += 1
    for i in alg:
        alghash[i] += ingr
        numalg[i] += 1

numing = {}
for i in alghash:
    numing[i] = defaultdict(lambda : 0)
    for j in alghash[i]:
        numing[i][j] += 1

print(ingrhash)
print(alghash)
print(foods)
print(numalg)
print(numing)

while True:
    for i in numing:
        if i in finalalg:
            continue
        poten = []
        for j in numing[i]:
            if j in finalingr:
                continue
            if numing[i][j] == numalg[i]:
                poten.append(j)
        if len(poten) == 1:
            finalalg[i] = poten[0]
            finalingr[poten[0]] = i
    if len(numalg) == len(finalalg):
        break

print(finalingr)
print(finalalg)
print(finuming)
count = 0
for i in finuming:
    if i in finalingr:
        continue
    count += finuming[i]
print(count)

print(",".join(sorted(finalingr.keys(), key=lambda a : finalingr[a])))