import re
lights = {}
for y in range(1000):
    for x in range(1000):
        lights[str(y) + ',' + str(x)] = 0
step = 0
while True:
    try:
        instruction = input()
    except EOFError:
        break
    mg = re.match(r"(.+) (\d+),(\d+) through (\d+),(\d+)", instruction)
    operation = mg.group(1)
    xone = int(mg.group(2))
    yone = int(mg.group(3))
    xtwo = int(mg.group(4))
    ytwo = int(mg.group(5))

    if operation == "turn on":
        for y in range(yone, ytwo + 1):
            for x in range(xone, xtwo + 1):
                lights[str(x) + ',' + str(y)] += 1
    elif operation == "turn off":
        for y in range(yone, ytwo + 1):
            for x in range(xone, xtwo + 1):
                if lights [str(x) + ',' + str(y)] != 0:
                    lights[str(x) + ',' + str(y)] -= 1
    elif operation == "toggle":
        for y in range(yone, ytwo + 1):
            for x in range(xone, xtwo + 1):
                lights[str(x) + ',' + str(y)] += 2

    step += 1
    print(str(step) + "/300")
sumup = 0
for i in lights:
    sumup += lights[i]
print(sumup)
