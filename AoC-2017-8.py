from collections import defaultdict
registers = defaultdict(lambda : 0)

def execute(reg, op, val):
    if op == "inc":
        registers[reg] += val
    elif op == "dec":
        registers[reg] -= val
    else:
        print("unknown executive operator")
        exit(1)

def check(reg, op, val):
    if op == ">":
        if registers[reg] > val:
            return True
    elif op == "<":
        if registers[reg] < val:
            return True
    elif op == "==":
        if registers[reg] == val:
            return True
    elif op == ">=":
        if registers[reg] >= val:
            return True
    elif op == "<=":
        if registers[reg] <= val:
            return True
    elif op == "!=":
        if registers[reg] != val:
            return True
    else:
        print("unknown logical operator")
        exit(2)
    return False

maxval = 0
while True:
    try:
        inp = input().split(" ")
    except EOFError:
        break
    reg = inp[0]
    op = inp[1]
    opval = int(inp[2])
    checkreg = inp[4]
    checkop = inp[5]
    checkval = int(inp[6])
    if check(checkreg, checkop, checkval):
        execute(reg, op, opval)
    if max(registers.values()) > maxval:
        maxval = max(registers.values())
print(maxval)