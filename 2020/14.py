import re
maskmo = re.match(r"mask = (.+)", input())
mask = maskmo.group(1)
print(mask)

vals = {}
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
    binval = "{:0>36b}".format(value)
    for i in range(36):
        binvall = list(binval)
        if mask[i] == "1":
            binvall[i] = "1"
        elif mask[i] == "0":
            binvall[i] = "0"
        binval = "".join(binvall)
    valuetwo = int(binval, 2)
    vals[cell] = valuetwo
print(sum(vals.values()))



