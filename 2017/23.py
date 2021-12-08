instructions = []
registers = {"a" : 0, "b" : 0, "c" : 0, "d" : 0, "e" : 0, "f" : 0, "g" : 0, "h" : 0}
while True:
    try:
        instructions.append(input().split(" "))
    except EOFError:
        break

index = 0
while True:
    try:
        ins = instructions[index][0]
        valone = instructions[index][1]
        valtwo = instructions[index][2]
    except IndexError:
        break

    if valtwo in list(registers.keys()):
        valtwo = int(registers[valtwo])
    else:
        valtwo = int(valtwo)

    if valone not in list(registers.keys()):
        valone = 1

    if ins == "set":
        registers[valone] = valtwo
    elif ins == "sub":
        registers[valone] -= valtwo
    elif ins == "mul":
        registers[valone] *= valtwo
    elif ins == "jnz":
        if valone != 0:
            index += valtwo - 1
        continue
    print(index)
    print(registers)
    index += 1