from collections import defaultdict

FILE_NAME = "2024/05.txt"
FILE_SIZE = 1374
PART = 2

rules = defaultdict(lambda : [])
def compare(a, b):
    if a in rules[b]:
        return False
    if b in rules[a]:
        return True

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
        result = compare(first, second)
        if result:
            continue
        else:
            proper = False
            break
    if proper and PART == 1:
        sum += s[len(s) // 2]
    elif not proper and PART == 2:
        for n in range(len(s) - 1, 0, -1):
            swapped = False  
            for i in range(n):
                if not compare(s[i], s[i + 1]):
                    s[i], s[i + 1] = s[i + 1], s[i]
                    swapped = True
            if not swapped:
                break
        sum += s[len(s) // 2]
print(sum)
        