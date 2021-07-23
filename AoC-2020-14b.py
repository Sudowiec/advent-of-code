import re
maskmo = re.match(r"mask = (.+)", input())
mask = maskmo.group(1)

valhash = {}
while True:
    try:
        inp = input()
    except EOFError:
        break

    if inp [1] == "a":
        maskmo = re.match(r"mask = (.+)", inp)
        mask = maskmo.group(1)
        continue

    mo = re.match(r"mem\[(\d+)\] = (\d+)", inp)
    cell = int(mo.group(1))
    value = int(mo.group(2))
    binval = "{:0>36b}".format(cell)

    floats = 0
    for i in range(36):
        binvall = list(binval)
        if mask[i] == "1":
            binvall[i] = "1"
        elif mask[i] == "X":
            binvall[i] = "X"
            floats += 1
        binval = "".join(binvall)
    # print(binval)
    # print(floats)


    for i in range(2**floats):
        binvall = list(binval)
        binfloat = ("{:0>" + str(floats) + "b}").format(i)
        binfloatl = list(binfloat)
        using = 0
        for j in range(36):
            if binvall[j] == "X":
                binvall[j] = binfloatl[using]
                using += 1
        newbinval = "".join(binvall)
        changedval = int(newbinval, 2)
        valhash[changedval] = value
print(valhash)
print(sum(valhash.values()))