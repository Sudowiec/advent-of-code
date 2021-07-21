import re
instructions = []
while True:
    try:
        instructions.append(input())
    except EOFError:
        break
index = 0
registers = {"a" : 1, "b" : 0}
while index < len(instructions):
    cur_ins = instructions[index]
    if cur_ins == "hlf a":
        registers["a"] = int(registers["a"] / 2)
    elif cur_ins == "tpl a":
        registers["a"] *= 3
    elif cur_ins[:3] == "inc":
        registers[cur_ins[4]] += 1
    elif cur_ins[:3] == "jmp":
        match = re.match(r"jmp (.*)", cur_ins)
        offset = int(match.group(1))
        index += offset
        continue
    elif cur_ins[:3] == "jie":
        reg = cur_ins[4]
        match = re.match(r"jie ., (.*)", cur_ins)
        offset = int(match.group(1))
        if registers[reg] % 2 == 0:
            index += offset
            continue
    elif cur_ins[:3] == "jio":
        reg = cur_ins[4]
        match = re.match(r"jio ., (.*)", cur_ins)
        offset = int(match.group(1))
        if registers[reg] == 1:
            index += offset
            continue
    index += 1
print(registers["b"])