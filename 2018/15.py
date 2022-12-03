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

# main loop
while True:
    for roundY in range(CAVEH):
        for roundX in range(CAVEW):
            if cave[roundY][roundX] != "G" and cave[roundY][roundX] != "E":
                continue

            