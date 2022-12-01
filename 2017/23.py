instructions = []
registers = {"a" : 0, "b" : 0, "c" : 0, "d" : 0, "e" : 0, "f" : 0, "g" : 0, "h" : 0}
while True:
    try:
        instructions.append(input().split(" "))
    except EOFError:
        break

index = 0
mulCount = 0

def getVal(ref):
    return registers[ref] if ref in registers.keys() else int(ref)

while True:
    try:
        ins = instructions[index][0]
        valone = instructions[index][1]
        valtwo = getVal(instructions[index][2])
    except IndexError:
        break

    if ins == "set":
        registers[valone] = valtwo
    elif ins == "sub":
        registers[valone] -= valtwo
    elif ins == "mul":
        registers[valone] *= valtwo
        mulCount += 1
    
    index += valtwo if ins == 'jnz' and getVal(valone) != 0 else 1
print(mulCount)