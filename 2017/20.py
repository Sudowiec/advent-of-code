import re
# initialization
particles = []
while True:
    try:
        inp = input()
    except EOFError:
        break
    mg = re.match(r"p=<(.+),(.+),(.+)>, v=<(.+),(.+),(.+)>, a=<(.+),(.+),(.+)>", inp)
    particles.append({"p": [int(mg.group(1)), int(mg.group(2)), int(mg.group(3))],
                      "v": [int(mg.group(4)), int(mg.group(5)), int(mg.group(6))],
                      "a": [int(mg.group(7)), int(mg.group(8)), int(mg.group(9))]})

while True:
    # movement
    for part in particles:
        for i in range(3):
            part["v"][i] += part["a"][i]
        for i in range(3):
            part["p"][i] += part["v"][i]

    # distance from zero
    furthest = 9999999
    lfparticle = -1
    for part in particles:
        val = abs(part["p"][0]) + abs(part["p"][1]) + abs(part["p"][2])
        if val < furthest:
            furthest = val
            lfparticle = particles.index(part)
    print(lfparticle)