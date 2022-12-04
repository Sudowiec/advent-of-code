CAVEH = 0
CAVEW = 0
INF = 9999999

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
    startCoords = [currentNpc["Y"], currentNpc["X"]]
    beenTo = []
    reachable = []
    queue = []

    def rec(coords, dist):
        y = coords[0]
        x = coords[1]
        beenTo.append([y, x])
        print(queue)
        if cave[y][x - 1] == "." and [y, x - 1] not in beenTo: # left
            elemd = [y, x - 1, dist]
            elem = [y, x - 1]
            reachable.append(elemd)
            if elem not in beenTo and elem not in queue:
                queue.append(elem)
            queue.append([y, x - 1])
        if cave[y][x + 1] == "." and [y, x + 1] not in beenTo: # right
            elemd = [y, x + 1, dist]
            elem = [y, x + 1]
            reachable.append(elemd)
            if elem not in beenTo and elem not in queue:
                queue.append(elem)
        if cave[y - 1][x] == "." and [y - 1, x] not in beenTo: # up
            elemd = [y - 1, x, dist]
            elem = [y - 1, x]
            reachable.append(elemd)
            if elem not in beenTo and elem not in queue:
                queue.append(elem)
        if cave[y + 1][x] == "." and [y + 1, x] not in beenTo: # down
            elemd = [y + 1, x, dist]
            elem = [y + 1, x]
            reachable.append(elemd)
            if elem not in beenTo and elem not in queue:
                queue.append(elem)
        if len(queue) > 0:
            rec(queue.pop(0), dist + 1)
        return

    rec(startCoords, 1)
    return reachable

print(getReachable({"Y" : 3, "X" : 2}))
# get nearest tiles from a tileset
def getNearest(currentNpc, tileset):
    queue = []
    def bfs(coords, dist):
        y = coords[0]
        x = coords[1]
        
    



# main loop
while True:
    for roundY in range(CAVEH):
        for roundX in range(CAVEW):
            if cave[roundY][roundX] != "G" and cave[roundY][roundX] != "E":
                continue

            