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
                      "a": [int(mg.group(7)), int(mg.group(8)), int(mg.group(9))],
                      "r" : 0})


while True:
    # movement
    for part in particles:
        if part["r"] == 1:
            continue
        for i in range(3):
            part["v"][i] += part["a"][i]
        for i in range(3):
            part["p"][i] += part["v"][i]

    # finding collisions
    for i in range(len(particles)):
        if particles[i]["r"] == 1:
            continue
        for j in range(i, len(particles)):
            if i == j or particles[j]["r"] == 1:
                continue
            if particles[i]["p"] == particles[j]["p"]:
                particles[i]["r"] = 1
                particles[j]["r"] = 1

    amount = 1000
    for part in particles:
        if part["r"] == 1:
            amount -= 1
    print(amount)

