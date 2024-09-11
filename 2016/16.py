import sys, math

INIT = "10001110011110000"
DISK_SIZE = 35651584

def dragon_curve(inp):
    a = inp
    b = list(a[::-1])
    for i in range(len(b)):
        b[i] = str((int(b[i]) + 1) % 2)
    b = "".join(b)
    return f"{a}0{b}"

def check_sum(inp):
    while True:
        if (len(inp) % 2) == 1:
            return inp
        new_inp = ""
        for i in range(0, len(inp) - 1, 2):
            if len(set(inp[i : i + 2])) == 1:
                new_inp += "1"
            else:
                new_inp += "0"
        inp = new_inp

current = INIT
while True:
    if len(current) >= DISK_SIZE:
        current = current[:DISK_SIZE]
        break
    current = dragon_curve(current)
print(check_sum(current))