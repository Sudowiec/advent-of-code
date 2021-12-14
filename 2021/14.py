from collections import defaultdict
ITERATIONS = 40
polymer = list(input())
input()
rules = {}
print("".join(polymer))

while True:
    try:
        inp = input().split(" -> ")
    except EOFError:
        break
    rules[inp[0]] = inp[1]

for interat in range(ITERATIONS):
    toins = []
    for i in range(1, len(polymer)):
        pair = polymer[i - 1] + polymer[i]
        toins.append(rules[pair])
    pos = 1
    offset = 0
    while len(toins) > 0:
        polymer.insert(pos + offset, toins.pop(0))
        offset += 1
        pos += 1
    print(interat, "".join(polymer))

counter = defaultdict(lambda : 0)
for i in polymer:
    counter[i] += 1
print(max(counter.values()))
print(min(counter.values()))
print(max(counter.values()) - min(counter.values()))
