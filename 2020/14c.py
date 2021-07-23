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

    maskzero = re.sub(r"X", "0", mask)
    maskone = re.sub(r"X", "1", mask)
    maskzero = int(maskzero, 2)
    maskone = int(maskone, 2)

    b = value | maskzero
    vals[cell] = b & maskone

print(sum(vals.values()))