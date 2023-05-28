hpos = {"x" : 1, "y" : 1}
tpos = {"x" : 1, "y" : 1}

def translate(pos, op):
    if op == "S":
        pass
    elif op == "D":
        pos["y"] -= 1
    elif op == "U":
        pos["y"] += 1
    elif op == "R":
        pos["x"] += 1
    elif op == "L":
        pos["x"] -= 1
    elif op == "LD":
        pos["x"] -= 1
        pos["y"] -= 1
    elif op == "LU":
        pos["x"] -= 1
        pos["y"] += 1
    elif op == "RD":
        pos["x"] += 1
        pos["y"] -= 1
    elif op == "RU":
        pos["x"] += 1
        pos["y"] += 1
    else:
        print("err")
        exit(1)
    return pos

def getRelativePos():
    if hpos["x"] == tpos["x"] and hpos["y"] == tpos["y"]:
        return "S"
    elif hpos["x"] == tpos["x"] and hpos["y"] < tpos["y"]:
        return "D"
    elif hpos["x"] == tpos["x"] and hpos["y"] > tpos["y"]:
        return "U"
    elif hpos["x"] < tpos["x"] and hpos["y"] == tpos["y"]:
        return "L"
    elif hpos["x"] > tpos["x"] and hpos["y"] == tpos["y"]:
        return "R"
    elif hpos["x"] < tpos["x"] and hpos["y"] < tpos["y"]:
        return "LD"
    elif hpos["x"] < tpos["x"] and hpos["y"] > tpos["y"]:
        return "LU"
    elif hpos["x"] > tpos["x"] and hpos["y"] < tpos["y"]:
        return "RD"
    elif hpos["x"] > tpos["x"] and hpos["y"] > tpos["y"]:
        return "RU"
    else:
        print("err")
        exit(2)

def nextTailMove(op):
    hcur = getRelativePos()
    if hcur == op:
        return op
    elif hcur == "LD" and (op == "D" or op == "L"):
        return "LD"
    elif hcur == "RD" and (op == "D" or op == "R"):
        return "RD"
    elif hcur == "LU" and (op == "U" or op == "L"):
        return "LU"
    elif hcur == "RU" and (op == "U" or op == "R"):
        return "RU"
    else:
        return "S"

inp = open("2022/09.txt")
seen = []
while True:
    ins = inp.readline().strip()
    if ins == "":
        break
    direction = ins.split(" ")[0]
    times = int(ins.split(" ")[1])
    for i in range(times):
        tpos = translate(tpos, nextTailMove(direction))
        hpos = translate(hpos, direction)
        seen.append(str(tpos["x"]) + "," + str(tpos["y"]))
seen = set(seen)
print(len(seen))