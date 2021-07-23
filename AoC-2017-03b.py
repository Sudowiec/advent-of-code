inp = 325489

amplitudex = 0
x = 0
dirx = 1
amplitudey = 0
y = 0
diry = 0

valhash = {(0, 0) : 1}

def valuing(x, y):
    global valhash
    sum = 0

    try:
        sum += valhash[(x + 1, y)]
    except KeyError:
        pass
    try:
        sum += valhash[(x - 1, y)]
    except KeyError:
        pass
    try:
        sum += valhash[(x + 1, y + 1)]
    except KeyError:
        pass
    try:
        sum += valhash[(x - 1, y + 1)]
    except KeyError:
        pass
    try:
        sum += valhash[(x + 1, y - 1)]
    except KeyError:
        pass
    try:
        sum += valhash[(x - 1, y - 1)]
    except KeyError:
        pass
    try:
        sum += valhash[(x, y - 1)]
    except KeyError:
        pass
    try:
        sum += valhash[(x, y + 1)]
    except KeyError:
        pass

    return sum

while True:
    found = False
    if dirx % 2 == 0:
        for i in range(amplitudex):
            x += 1
            s = valuing(x, y)
            valhash[(x, y)] = s
            print(x, y, s)
            if s > inp:
                exit(0)
    elif dirx % 2 == 1:
        for i in range(amplitudex):
            x -= 1
            s = valuing(x, y)
            valhash[(x, y)] = s
            print(x, y, s)
            if s > inp:
                exit(0)

    if diry % 2 == 0:
        for i in range(amplitudey):
            y -= 1
            s = valuing(x, y)
            valhash[(x, y)] = s
            print(x, y, s)
            if s > inp:
                exit(0)
    elif diry % 2 == 1:
        for i in range(amplitudey):
            y += 1
            s = valuing(x, y)
            valhash[(x, y)] = s
            print(x, y, s)
            if s > inp:
                exit(0)

    dirx += 1
    amplitudex += 1
    diry += 1
    amplitudey += 1
