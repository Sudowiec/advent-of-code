import copy

scheme = []
turnlist = ["L", "U", "R", "D"]
crosslist = ["L", "S", "R"]
while True:
    try:
        inp = list(input())
    except EOFError:
        break
    scheme.append(inp)

def printgrid(matrix):
    for i in matrix:
        print("".join(i))

maxy = len(scheme) - 1
maxx = 0
for i in scheme:
    if len(i) > maxx:
        maxx = len(i) - 1

for i in range(len(scheme)):
    if len(scheme[i]) < maxx + 1:
        diff = abs(len(scheme[i]) - maxx - 1)
        for j in range(diff):
            scheme[i].append(" ")
# printgrid(scheme)

carts = {}
cartsdirs = {}
indx = 0
for y in range(maxy + 1):
    for x in range(maxx + 1):
        if scheme[y][x] == "v" or scheme[y][x] == ">" or scheme[y][x] == "<" or scheme[y][x] == "^":
            carts[indx] = str(y) + "," + str(x)
            if scheme[y][x] == "v":
                cartsdirs[indx] = "D,0"
            elif scheme[y][x] == "^":
                cartsdirs[indx] = "U,0"
            elif scheme[y][x] == ">":
                cartsdirs[indx] = "R,0"
            elif scheme[y][x] == "<":
                cartsdirs[indx] = "L,0"
            else:
                print("Fatal Error")
                exit(2)
            indx += 1
# print(carts)

for i in carts:
    carty = int(carts[i].split(",")[0])
    cartx = int(carts[i].split(",")[1])
    cartdir = cartsdirs[i].split(",")[0]

    if cartdir == "L" or cartdir == "R":
        scheme[carty][cartx] = "-"
    else:
        scheme[carty][cartx] = "|"
    preview = copy.deepcopy(scheme)

notcrashedcarts_id = []
for i in carts:
    notcrashedcarts_id.append(i)
# print(notcrashedcarts_id)

while True:
    for i in carts:
        if i not in notcrashedcarts_id:
            continue

        carty = int(carts[i].split(",")[0])
        cartx = int(carts[i].split(",")[1])
        cartdir = cartsdirs[i].split(",")[0]
        cartturn = int(cartsdirs[i].split(",")[1])

        scheme[carty][cartx] = preview[carty][cartx]

        if cartdir == "L":
            cartx -= 1
        elif cartdir == "R":
            cartx += 1
        elif cartdir == "U":
            carty -= 1
        elif cartdir == "D":
            carty += 1
        else:
            print("Text error")
            exit(3)

        if len(notcrashedcarts_id) == 1:
            print(str(cartx) + "," + str(carty))
            exit(0)

        next_step = scheme[carty][cartx]
        if next_step == "|":
            if cartdir == "U":
                scheme[carty][cartx] = "^"
            elif cartdir == "D":
                scheme[carty][cartx] = "v"

        elif next_step == "-":
            if cartdir == "L":
                scheme[carty][cartx] = "<"
            elif cartdir == "R":
                scheme[carty][cartx] = ">"

        elif next_step == "/":
            if cartdir == "U":
                scheme[carty][cartx] = ">"
                cartdir = "R"
            elif cartdir == "D":
                scheme[carty][cartx] = "<"
                cartdir = "L"
            elif cartdir == "R":
                scheme[carty][cartx] = "^"
                cartdir = "U"
            elif cartdir == "L":
                scheme[carty][cartx] = "v"
                cartdir = "D"

        elif next_step == "/":
            if cartdir == "U":
                scheme[carty][cartx] = ">"
                cartdir = "R"
            elif cartdir == "D":
                scheme[carty][cartx] = "<"
                cartdir = "L"
            elif cartdir == "R":
                scheme[carty][cartx] = "^"
                cartdir = "U"
            elif cartdir == "L":
                scheme[carty][cartx] = "v"
                cartdir = "D"

        elif next_step == "\\":
            if cartdir == "U":
                scheme[carty][cartx] = "<"
                cartdir = "L"
            elif cartdir == "D":
                scheme[carty][cartx] = ">"
                cartdir = "R"
            elif cartdir == "R":
                scheme[carty][cartx] = "v"
                cartdir = "D"
            elif cartdir == "L":
                scheme[carty][cartx] = "^"
                cartdir = "U"

        elif next_step == "+":
            if cartdir == "U":
                if cartturn == 0:
                    scheme[carty][cartx] = "<"
                    cartdir = "L"
                    cartturn = 1
                elif cartturn == 1:
                    scheme[carty][cartx] = "^"
                    cartturn = 2
                elif cartturn == 2:
                    scheme[carty][cartx] = ">"
                    cartdir = "R"
                    cartturn = 0
            elif cartdir == "D":
                if cartturn == 0:
                    scheme[carty][cartx] = ">"
                    cartdir = "R"
                    cartturn = 1
                elif cartturn == 1:
                    scheme[carty][cartx] = "v"
                    cartturn = 2
                elif cartturn == 2:
                    scheme[carty][cartx] = "<"
                    cartdir = "L"
                    cartturn = 0
            elif cartdir == "R":
                if cartturn == 0:
                    scheme[carty][cartx] = "^"
                    cartdir = "U"
                    cartturn = 1
                elif cartturn == 1:
                    scheme[carty][cartx] = ">"
                    cartturn = 2
                elif cartturn == 2:
                    scheme[carty][cartx] = "v"
                    cartdir = "D"
                    cartturn = 0
            elif cartdir == "L":
                if cartturn == 0:
                    scheme[carty][cartx] = "v"
                    cartdir = "D"
                    cartturn = 1
                elif cartturn == 1:
                    scheme[carty][cartx] = "<"
                    cartturn = 2
                elif cartturn == 2:
                    scheme[carty][cartx] = "^"
                    cartdir = "U"
                    cartturn = 0

        elif next_step == "v" or next_step == "^" or next_step == ">" or next_step == "<":
            scheme[carty][cartx] = preview[carty][cartx]
            for j in carts:
                ycheck = int(carts[j].split(",")[0])
                xcheck = int(carts[j].split(",")[1])
                if ycheck == carty and xcheck == cartx:
                    notcrashedcarts_id.remove(j)
                    notcrashedcarts_id.remove(i)
                    break

        carts[i] = str(carty) + "," + str(cartx)
        cartsdirs[i] = cartdir + "," + str(cartturn)
    # printgrid(scheme)
    # print(notcrashedcarts_id)




