import re
reins = {}
reinset = []

while True:
    try:
        inp = input()
    except EOFError:
        break
    mo = re.match(r"(.+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds", inp)
    rein = mo.group(1)
    speed = mo.group(2)
    time = mo.group(3)
    rest = mo.group(4)
    reins[rein] = {"speed" : int(speed), "time" : int(time), "rest" : int(rest), "km" : 0, "resting" : False, "timeleft" : int(time), "points" : 0}
    reinset.append(rein)
reinset = set(reinset)


for second in range(1, 2504):

    leaderboard = {}
    for i in reinset:
        leaderboard[i] = 0

    for i in reinset:
        if not reins[i]["resting"]:
            reins[i]["km"] += reins[i]["speed"]
            reins[i]["timeleft"] -= 1
            if reins[i]["timeleft"] == 0:
                reins[i]["resting"] = True
                reins[i]["timeleft"] = reins[i]["rest"]
        else:
            reins[i]["timeleft"] -= 1
            if reins[i]["timeleft"] == 0:
                reins[i]["resting"] = False
                reins[i]["timeleft"] = reins[i]["time"]
        leaderboard[i] = reins[i]["km"]
    print(leaderboard)
    winner = ""
    highest = 0
    for i in leaderboard:
        if leaderboard[i] > highest:
            highest = leaderboard[i]
            winner = i
    for i in leaderboard:
        if leaderboard[i] == highest:
            reins[i]["points"] += 1
    print(reins[winner])


for i in reins:
    print(i, reins[i]["points"])