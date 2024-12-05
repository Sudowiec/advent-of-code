from collections import defaultdict

FILE_NAME = "2024/05.txt"
FILE_SIZE = 1374

rules = defaultdict(lambda : [])
sets = []
f = open(FILE_NAME, "r")
for line_number in range(FILE_SIZE):
    inp = f.readline().strip()
    if "|" in inp:
        rules[int(inp.split("|")[0])].append(int(inp.split("|")[1]))
    elif "," in inp:
        sets.append(list(map(int, inp.split(","))))

sum = 0
for s in sets:
    proper = True
    for i in range(len(s) - 1):
        first = s[i]
        second = s[i + 1]
        if second in rules[first]:
            continue
        if first in rules[second]:
            proper = False
            break
    if proper:
        sum += s[len(s) // 2]
print(sum)
        