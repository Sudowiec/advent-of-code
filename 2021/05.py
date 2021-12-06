from collections import defaultdict
points = defaultdict(lambda : 0)
while True:
    try:
        inp = input().split(" -> ")
    except EOFError:
        break
    x1 = int(inp[0].split(",")[0])
    x2 = int(inp[1].split(",")[0])
    y1 = int(inp[0].split(",")[1])
    y2 = int(inp[1].split(",")[1])

    genx = []
    if x2 - x1 > 0:
        for i in range(x1, x2 + 1):
            genx.append(i)
    elif x2 - x1 < 0:
        for i in range(x1, x2 - 1, -1):
            genx.append(i)

    geny = []
    if y2 - y1 > 0:
        for i in range(y1, y2 + 1):
            geny.append(i)
    elif y2 - y1 < 0:
        for i in range(y1, y2 - 1, -1):
            geny.append(i)

    print(genx, geny)

    if len(genx) > len(geny):
        for i in range(len(genx)):
            points[str(genx[i]) + "," + str(y1)] += 1
            print(str(genx[i]) + "," + str(y1))
    elif len(genx) < len(geny):
        for i in range(len(geny)):
            points[str(x1) + "," + str(geny[i])] += 1
            print(str(x1) + "," + str(geny[i]))
    else:
        for i in range(len(geny)):
            points[str(genx[i]) + "," + str(geny[i])] += 1
            print(str(genx[i]) + "," + str(geny[i]))

print(points)
counter = 0
for i in points:
    if points[i] > 1:
        counter += 1
print(counter)