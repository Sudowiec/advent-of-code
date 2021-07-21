import time
# firewall initialization
prefirewall = {}
maxval = 0
while True:
    try:
        inp = list(map(int, input().split(": ")))
        if inp[0] > maxval:
            maxval = inp[0]
        prefirewall[inp[0]] = inp[1]
    except EOFError:
        break
firewall = {}
for i in range(maxval + 1):
    if i in prefirewall:
        firewall[i] = prefirewall[i]
    else:
        firewall[i] = 0
print(firewall)

delaycount = 0
brokethrough = False
while True:
    # scanners initialization
    scanners = {}
    for i in prefirewall:
        scanners[i] = {"pos": 0, "range": prefirewall[i] - 1, "movement": "down"}
    package = {"pos": -1}
    delay = delaycount
    # print(delaycount)
    while True:
        # package movement
        if delay == 0:
            package["pos"] += 1
            if package["pos"] > maxval: #got to end
                brokethrough = True
                break
            if package["pos"] in scanners:
                if scanners[package["pos"]]["pos"] == 0: #caught
                    delaycount += 1
                    break
        else:
            delay -= 1

        # scanners movement
        for i in scanners:
            if scanners[i]["movement"] == "down":
                scanners[i]["pos"] += 1
            elif scanners[i]["movement"] == "up":
                scanners[i]["pos"] -= 1
            else:
                print("Error: unrecognised movement order")
                exit(1)

            if scanners[i]["movement"] == "up" and scanners[i]["pos"] == 0:
                scanners[i]["movement"] = "down"
            elif scanners[i]["movement"] == "down" and scanners[i]["pos"] == scanners[i]["range"]:
                scanners[i]["movement"] = "up"
        # print(scanners)
    if brokethrough:
        print(delaycount)
        break