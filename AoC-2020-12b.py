ins = []

while True:
    try:
        inp = input()
    except EOFError:
        break
    ins.append((inp[:1], int(inp[1:])))

wp = {"x" : 10, "y" : 1}
ship = {"x" : 0, "y" : 0}

for i in ins:
    dir = i[0]
    val = i[1]
    if dir == "N":
        wp["y"] += val
    elif dir == "S":
        wp["y"] -= val
    elif dir == "E":
        wp["x"] += val
    elif dir == "W":
        wp["x"] -= val
    elif dir == "R":
        for num in range(int(val / 90)):
            wp["x"] , wp["y"] = wp["y"] , -wp["x"]
    elif dir == "L":
        for num in range(int(val / 90)):
            wp["x"] , wp["y"] = -wp["y"] , wp["x"]
    elif dir == "F":
        ship["x"] += wp["x"] * val
        ship["y"] += wp["y"] * val
print(abs(ship["x"]) + abs(ship["y"]))
