inps = [0]
while True:
    try:
        inps.append(int(input()))
    except EOFError:
        break
inps.sort()
inps = list(range(34))
last = max(inps) + 3
inps.append(last)
print(inps)

diffs = {1 : 0, 2 : 0, 3 : 0}
for i in range(1, len(inps)):
    diffs[inps[i] - inps[i - 1]] += 1

print(diffs)
print(diffs[1] * diffs[3])
hashinp = {}
for i in inps:
    hashinp[i] = True

cache = {}
def summer(num):
    global cache
    sumup = 0
    if num == 0:
        return 1
    for i in range(1, 4):
        if num - i in cache:
            sumup += cache[num - i]
        elif num - i in inps:
            sumup += summer(num - i)
    cache[num] = sumup
    return sumup

print(summer(last))