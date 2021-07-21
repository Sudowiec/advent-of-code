import re
from collections import defaultdict
refs = {}
vals = {}

def valuer(ins):
    if ins in vals:
        return (vals[ins])
    elif ins.isdigit():
        return (int(ins))
    else:
        vals[ins] = solve(ins)
        return (vals[ins])

def solve(reg):
    global refs
    ins = refs[reg]
    insmthree = re.match(r"(\S+) (AND|OR|RSHIFT|LSHIFT) (\S+)", ins)
    insmtwo = re.match(r"NOT (\S+)", ins)
    if insmthree:
        a = valuer(insmthree.group(1))
        b = valuer(insmthree.group(3))
        group = insmthree.group(2)
        if group == "AND":
            return a & b
        elif group == "OR":
            return a | b
        elif group == "RSHIFT":
            return a >> b
        elif group == "LSHIFT":
            return a << b
        else:
            print("DIE")
            exit(2)
    elif insmtwo:
        return ~valuer(insmtwo.group(1))
    else:
        return valuer(ins)
while True:
    try:
        inp = input()
    except EOFError:
        break
    mg = re.match(r"(.+) -> (.+)", inp)
    reg = mg.group(2)
    ins = mg.group(1)
    refs[reg] = ins
print(refs)

a = solve("a")
vals = {"b" : a}
print(solve("a"))
