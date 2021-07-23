inp = 325489

amplitudex = 0
x = 0
dirx = 1
amplitudey = 0
y = 0
diry = 0
counter = 1
while counter <= inp:
    found = False
    if dirx % 2 == 0:
        for i in range(amplitudex):
            x += 1
            print(x, y, counter + 1)
            counter += 1
            if counter == inp:
                found = True
                break
    elif dirx % 2 == 1:
        for i in range(amplitudex):
            x -= 1
            print(x, y, counter + 1)
            counter += 1
            if counter == inp:
                found = True
                break

    if found:
        break

    if diry % 2 == 0:
        for i in range(amplitudey):
            y -= 1
            print(x, y, counter + 1)
            counter += 1
            if counter == inp:
                found = True
                break
    elif diry % 2 == 1:
        for i in range(amplitudey):
            y += 1
            print(x, y, counter + 1)
            counter += 1
            if counter == inp:
                found = True
                break

    if found:
        break

    dirx += 1
    amplitudex += 1
    diry += 1
    amplitudey += 1
print(x, y, abs(x) + abs(y))