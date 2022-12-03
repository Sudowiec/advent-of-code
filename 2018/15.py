CAVEH = 0
CAVEW = 0

cave = []
npcs = []

# read input
while True:
    try:
        inp = list(input())
    except EOFError:
        break

    for i in range(len(inp)):
        if inp[i] == "G" or inp[i] == "E":
            npcs.append({"TYPE" : inp[i], "X" : i, "Y" : len(cave), "HP" : 200})
    
    cave.append(inp)
CAVEH = len(cave)
CAVEW = len(cave[0])

# get tiles in range function
def getInRange(currentNpc = None):
    inRange = []
    for npc in npcs:
        if currentNpc == npc:
            continue
        curX = npc["X"]
        curY = npc["Y"]
        curRanges = []
        curRanges.append([curY, curX - 1] if cave[curY][curX - 1] == "." else "DELETEME") # left
        curRanges.append([curY, curX + 1] if cave[curY][curX + 1] == "." else "DELETEME") # right
        curRanges.append([curY - 1, curX] if cave[curY - 1][curX] == "." else "DELETEME") # up
        curRanges.append([curY + 1, curX] if cave[curY + 1][curX] == "." else "DELETEME") # down
        inRange.extend(curRanges)
    inRangeSet = []
    [inRangeSet.append(i) for i in inRange if i != "DELETEME" and i not in inRangeSet]
    return inRangeSet

# get reachable tiles function
def getReachable(currentNpc):
    startX = currentNpc["X"]
    startY = currentNpc["Y"]
    beenTo = []
    reachable = []

    def rec(y, x):
        beenTo.append([y, x])
        if cave[y][x - 1] == "." and [y, x - 1] not in beenTo: # left
            reachable.append([y, x - 1])
            rec(y, x - 1)
        if cave[y][x + 1] == "." and [y, x + 1] not in beenTo: # right
            reachable.append([y, x + 1])
            rec(y, x + 1)
        if cave[y - 1][x] == "." and [y - 1, x] not in beenTo: # up
            reachable.append([y - 1, x])
            rec(y - 1, x)
        if cave[y + 1][x] == "." and [y + 1, x] not in beenTo: # down
            reachable.append([y + 1, x])
            rec(y + 1, x)
        return

    rec(startY, startX)
    return reachable

# main loop
while True:
    for roundY in range(CAVEH):
        for roundX in range(CAVEW):
            if cave[roundY][roundX] != "G" and cave[roundY][roundX] != "E":
                continue

            