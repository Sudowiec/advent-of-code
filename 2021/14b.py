from collections import defaultdict
ITER = 10
beginning = input()
rules = {}
pairscount = {}
input()
while True:
    try:
        inp = input().split(" -> ")
    except EOFError:
        break
    rules[inp[0]] = inp[1]
    pairscount[inp[0]] = 0

for i in range(1, len(beginning)):
    pairscount[beginning[i - 1] + beginning[i]] += 1
for indx in range(ITER):
    pairstoadd = []
    numtoadd = []
    for i in pairscount:
        if pairscount[i] == 0:
            continue
        letter = rules[i]
        pairstoadd.append(i[:1] + letter)
        numtoadd.append(pairscount[i])
        pairstoadd.append(letter + i[1:])
        numtoadd.append(pairscount[i])
        pairscount[i] -= 1
    for i in pairstoadd:
        pairscount[i] += numtoadd.pop(0)
    print(len(pairstoadd))
    print(pairscount)
letterscount = defaultdict(lambda : 0)
for i in pairscount:
    letterscount[i[:1]] += pairscount[i]
print(pairscount)
print(letterscount)