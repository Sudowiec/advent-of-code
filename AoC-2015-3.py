from collections import defaultdict
houses = defaultdict(lambda : 0)
houses["0,0"] = 1
inshashx = {"^" : 0, "v" : 0, "<" : -1, ">" : 1}
inshashy = {"^" : 1, "v" : -1, "<" : 0, ">" : 0}
instructions = list(input())
instructions_s = []
instructions_r = []
for i in range(len(instructions)):
    if i % 2 == 0:
        instructions_s.append(instructions[i])
    else:
        instructions_r.append(instructions[i])
print(instructions_s, instructions_r)

houses["0,0"] += 1
x = 0
y = 0
for i in instructions_s:
    x += inshashx[i]
    y += inshashy[i]
    houses[str(x) + ',' + str(y)] += 1

houses["0,0"] += 1
x = 0
y = 0
for i in instructions_r:
    x += inshashx[i]
    y += inshashy[i]
    houses[str(x) + ',' + str(y)] += 1
print(len(houses))