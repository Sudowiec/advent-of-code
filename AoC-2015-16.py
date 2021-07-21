import re
model = ["children", "cats", "samoyeds", "pomeranians", "akitas", "vizslas", "goldfish", "trees", "cars", "perfumes"]
modelsue = {"children" : 3, "cats" : 7, "samoyeds" : 2, "pomeranians" : 3, "akitas" : 0, "vizslas" : 0, "goldfish" : 5, "trees" : 3, "cars" : 2, "perfumes" : 1}
sues = []

while True:
    try:
        inp = input()
    except EOFError:
        break
    mo = re.search(": (.+): (\d+), (.+): (\d+), (.+): (\d+)", inp)
    aspects = {}
    for i in range(1, 7, 2):
        aspects[mo.group(i)] = int(mo.group(i + 1))

    prehash = {}
    for i in model:
        if i in aspects:
            prehash[i] = aspects[i]
        else:
            prehash[i] = -1
    sues.append(prehash)
print(sues)

indx = 1
for sue in sues:
    isthatsue = True
    if sue["children"] != modelsue["children"] and sue["children"] != -1:
        isthatsue = False
    if sue["cats"] <= modelsue["cats"] and sue["cats"] != -1:
        isthatsue = False
    if sue["samoyeds"] != modelsue["samoyeds"] and sue["samoyeds"] != -1:
        isthatsue = False
    if sue["pomeranians"] >= modelsue["pomeranians"] and sue["pomeranians"] != -1:
        isthatsue = False
    if sue["akitas"] != modelsue["akitas"] and sue["akitas"] != -1:
        isthatsue = False
    if sue["vizslas"] != modelsue["vizslas"] and sue["vizslas"] != -1:
        isthatsue = False
    if sue["goldfish"] >= modelsue["goldfish"] and sue["goldfish"] != -1:
        isthatsue = False
    if sue["trees"] <= modelsue["trees"] and sue["trees"] != -1:
        isthatsue = False
    if sue["cars"] != modelsue["cars"] and sue["cars"] != -1:
        isthatsue = False
    if sue["perfumes"] != modelsue["perfumes"] and sue["perfumes"] != -1:
        isthatsue = False
    if isthatsue:
        print(indx)
    indx += 1

