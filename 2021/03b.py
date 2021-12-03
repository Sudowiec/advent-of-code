import copy
BYTELEN = 12

vals = []
while True:
    try:
        vals.append(input())
    except EOFError:
        break

newvals = copy.deepcopy(vals)
bit = 0
while True:
    counter = {"0" : 0, "1" : 0}
    for i in newvals:
        counter[i[bit]] += 1
    higher = "1" if counter["1"] >= counter["0"] else "0"
    newnewvals = []
    for i in newvals:
        if i[bit] == higher:
            newnewvals.append(i)

    if len(newnewvals) == 1:
        break
    print(newnewvals)
    newvals = newnewvals
    bit += 1
oxygen = int(newnewvals[0], 2)

newvals = copy.deepcopy(vals)
bit = 0
while True:
    counter = {"0" : 0, "1" : 0}
    for i in newvals:
        counter[i[bit]] += 1
    lower = "0" if counter["0"] <= counter["1"] else "1"
    newnewvals = []
    for i in newvals:
        if i[bit] == lower:
            newnewvals.append(i)

    if len(newnewvals) == 1:
        break
    print(newnewvals)
    newvals = newnewvals
    bit += 1
print(newnewvals)
cotwo = int(newnewvals[0], 2)
print(oxygen, cotwo, oxygen*cotwo)