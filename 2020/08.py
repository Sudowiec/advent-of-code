import re
from collections import defaultdict
oginstructions = []
while True:
    try:
        inp = input()
    except EOFError:
        break
    mo = re.match(r"(.+) (.+)", inp)
    oginstructions.append({mo.group(1) : int(mo.group(2))})

accumulator = 0

for i in range(len(oginstructions)):

    instructions = oginstructions.copy()
    if "jmp" in oginstructions[i]:
        val = instructions[i]["jmp"]
        instructions[i] = {"nop" : val}
    elif "nop" in oginstructions[i]:
        val = instructions[i]["nop"]
        instructions[i] = {"jmp" : val}
    else:
        continue

    been_here = defaultdict(lambda: 0)
    accumulator = 0
    index = 0
    finished = True
    while index < len(instructions):
        been_here[index] += 1
        if 2 in been_here.values():
            finished = False
            print(accumulator)
            break
        if "acc" in instructions[index]:
            accumulator += instructions[index]['acc']
        elif "jmp" in instructions[index]:
            index += instructions[index]['jmp']
            continue
        index += 1
    if finished:
        print("Fin", accumulator)
        break