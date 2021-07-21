from collections import defaultdict
inps = []
bigsumup = 0
while True:
    try:
        inps.append(int(input()))
    except EOFError:
        break
length = len(inps)

conthash = defaultdict(lambda : 0)
for digit in range(2**length):
    containers = 0
    sumup = 0
    valid = True
    # print()
    for i in range(length):
        # print(digit & (1 << i))
        if (digit & (1 << i)) > 0:
            sumup += inps[i]
            containers += 1
        if sumup > 150:
            valid = False
            break
    if valid and sumup == 150:
        bigsumup += 1
        conthash[containers] += 1
print(conthash[min(conthash)])
print(bigsumup)