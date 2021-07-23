import re
code = 0
stringish = 0

def changer(mo):
    group = mo.group(1)
    if group == "\\\\":
        return "\\"
    elif group == "\\\"":
        return "\""
    else:
        hexish = group[2:]
        decish = int(hexish, 16)
        return chr(decish)

def secondchanger(mo):
    group = mo.group(1)
    if group == "\"":
        return "\\\""
    else:
        return "\\\\"


while True:
    try:
        inp = input()
    except EOFError:
        break
    code += len(inp)
    print(inp)
    # aftinp = re.sub(r"(\\\\|\\x..|\\\")", changer, inp)
    aftinp = re.sub(r"(\"|\\)", secondchanger, inp)
    aftinp = "\"" + aftinp + "\""
    print(aftinp)
    stringish += len(aftinp)
print(stringish - code)