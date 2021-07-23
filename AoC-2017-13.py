import time
# firewall initialization
prefirewall = {}
maxval = 0
while True:
    try:
        inp = list(map(int, input().split(": ")))
        prefirewall[inp[0]] = inp[1]
    except EOFError:
        break

delay = 0
while True:
    caught = False
    for i in prefirewall:
        tick = i
        depth = prefirewall[i]
        if (tick + delay) % (2 * (depth - 1)) == 0:
            # print(delay)
            caught = True
            delay += 1
            break
    if not caught:
        print(delay)
        break
