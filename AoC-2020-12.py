curdir = "E"
map = {"N" : 0, "W" : 0, "S" : 0, "E" : 0}
directions = ["N", "E", "S", "W"]
ins = []

while True:
    try:
        inp = input()
    except EOFError:
        break
    ins.append((inp[:1], int(inp[1:])))

for i in ins:
    dir = i[0]
    val = i[1]
    try:
        map[dir] += val
    except KeyError:
        if dir == "R":
            curdir = directions[(directions.index(curdir) + int(val / 90)) % 4]
        elif dir == "L":
            curdir = directions[(directions.index(curdir) - int(val / 90)) % 4]
        elif dir == "F":
            map[curdir] += val
print(abs(map["N"] - map["S"]) + abs(map["E"] - map["W"]))