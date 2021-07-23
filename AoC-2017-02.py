checksum = 0
evenly_dividing = 0
while True:
    try:
        inp = input()
    except EOFError:
        break
    inp = list(map(int, inp.split('\t')))
    maxval = 0
    minval = 99999
    for i in inp:
        if i > maxval:
            maxval = i
        if i < minval:
            minval = i
    checksum += maxval - minval
    for i in inp:
        for j in inp:
            if i % j == 0 and i != j:
                evenly_dividing += int(i / j)
print(checksum, evenly_dividing)
