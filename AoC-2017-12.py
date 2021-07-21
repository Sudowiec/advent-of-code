import time
pipehash = {}
points = []
while True:
    try:
        inp = input().split(" ")
    except EOFError:
        break
    id = int(inp[0])
    points.append(id)
    toadd = []
    for i in range(len(inp) - 2):
        toadd.append(int(inp[2 + i].replace(",", "")))
    pipehash[id] = toadd

counter = 0
while len(points) > 0:
    tryer = points[0]
    to_check = [tryer]
    in_group = []
    # print(pipehash)
    while len(to_check) > 0:
        tc = to_check.pop(0)
        in_group.append(tc)
        # print(tc)
        # print(to_check)
        checking = pipehash[tc]
        for i in checking:
            if i in in_group:
                continue
            else:
                to_check.append(i)
    in_group = list(set(in_group))
    for i in in_group:
        points.remove(i)
    counter += 1
print(counter)