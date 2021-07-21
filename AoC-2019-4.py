from collections import defaultdict
down = 245182
up = 790572
passwords = 0
for i in range(down, up + 1):
    strint = list(str(i))
    doublecheck = False
    doubles = defaultdict(lambda: 0)
    for j in strint:
        doubles[j] += 1
    for j in doubles:
        if doubles[j] == 2:
            doublecheck = True
    if doublecheck:
        risecheck = True
        testing = 0
        for j in strint:
            if int(j) < testing:
                risecheck = False
                break
            testing = int(j)
        if risecheck:
            passwords += 1
print(passwords)

