line = [{"x" : 1, "y" : 1} for i in range(10)]

def translate(pos, op):
    temppos = {"x" : pos["x"], "y" : pos["y"]}
    if op == "S":
        pass
    elif op == "D":
        temppos["y"] -= 1
    elif op == "U":
        temppos["y"] += 1
    elif op == "R":
        temppos["x"] += 1
    elif op == "L":
        temppos["x"] -= 1
    elif op == "LD":
        temppos["x"] -= 1
        temppos["y"] -= 1
    elif op == "LU":
        temppos["x"] -= 1
        temppos["y"] += 1
    elif op == "RD":
        temppos["x"] += 1
        temppos["y"] -= 1
    elif op == "RU":
        temppos["x"] += 1
        temppos["y"] += 1
    else:
        print("err")
        exit(1)
    return temppos

def getRelativePos(pos2, pos1):
    if pos1["x"] == pos2["x"] and pos1["y"] == pos2["y"]:
        return "S"
    elif pos1["x"] == pos2["x"] and pos1["y"] < pos2["y"]:
        return "D"
    elif pos1["x"] == pos2["x"] and pos1["y"] > pos2["y"]:
        return "U"
    elif pos1["x"] < pos2["x"] and pos1["y"] == pos2["y"]:
        return "L"
    elif pos1["x"] > pos2["x"] and pos1["y"] == pos2["y"]:
        return "R"
    elif pos1["x"] < pos2["x"] and pos1["y"] < pos2["y"]:
        return "LD"
    elif pos1["x"] < pos2["x"] and pos1["y"] > pos2["y"]:
        return "LU"
    elif pos1["x"] > pos2["x"] and pos1["y"] < pos2["y"]:
        return "RD"
    elif pos1["x"] > pos2["x"] and pos1["y"] > pos2["y"]:
        return "RU"
    else:
        print("err")
        exit(2)

def nextTailMove(op, pos1, pos2):
    hcur = getRelativePos(pos1, pos2)
    move = [hcur, op]
    if move in [["U", "U"], ["RU", "LU"], ["LU", "RU"]]:
        return "U"
    elif move in[["D", "D"], ["RD", "LD"], ["LD", "RD"]]:
        return "D"
    elif move in [["R", "R"], ["RU", "RD"], ["RD", "RU"]]:
        return "R"
    elif move in [["L", "L"], ["LU", "LD"], ["LD", "LU"]]:
        return "L"
    elif move in [["RU", "RU"], ["R", "RU"], ["U", "RU"], ["RU", "U"], ["RU", "R"]]:
        return "RU"
    elif move in [["RD", "RD"], ["D", "RD"],  ["R", "RD"],["RD", "D"], ["RD", "R"]]:
        return "RD"
    elif move in [["LU", "LU"], ["L", "LU"], ["U", "LU"], ["LU", "U"], ["LU", "L"]]:
        return "LU"
    elif move in [["LD", "LD"], ["L", "LD"], ["D", "LD"], ["LD", "D"], ["LD", "L"]]:
        return "LD"
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
        prevpos = {"x" : line[0]["x"], "y" : line[0]["y"]}
        prevdir = direction
        line[0] = translate(line[0], direction)
        for i in range(1, 10):
            ndir = nextTailMove(prevdir, line[i], prevpos)
            npos = translate(line[i], ndir)
            prevpos = {"x" : line[i]["x"], "y" : line[i]["y"]}
            line[i] = npos
            prevdir = ndir
        seen.append(str(line[9]["x"]) + "," + str(line[9]["y"]))
seen = set(seen)
print(len(seen))