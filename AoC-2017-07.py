pweights = {}
relations = {}
FIRST = "vgzejbd"
while True:
    try:
        inp = input().split(" ")
    except EOFError:
        break
    pweights[inp[0]] = int(inp[1][1:-1])
    relations[inp[0]] = []
    if len(inp) > 2:
        for i in inp[3:]:
            relations[inp[0]].append(i.replace(",", ""))
print(pweights)
print(relations)

def weight(vertex):
    wgt = pweights[vertex]
    for i in relations[vertex]:
        wgt += weight(i)
    return wgt

current = FIRST
while True:
    tocheck = relations[current]
    checkedweights = []
    for i in tocheck:
        checkedweights.append(weight(i))
    if len(set(checkedweights)) > 1:
        tb = max(checkedweights)
        ind = checkedweights.index(tb)
        current = tocheck[ind]
    else:
        imposter = current
        for j in relations:
            if imposter in relations[j]:
                prevtoimp = j
                break
        break
print(imposter)
lastweights = []
for i in relations[prevtoimp]:
    lastweights.append(weight(i))
print(pweights[imposter]- (max(lastweights) - min(lastweights)))
