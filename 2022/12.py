INF = 9999999
f = open("2022/12.txt")
highmap = []
while True:
    i = f.readline().strip()
    if i == "":
        break
    highmap.append(list("#" + i + "#"))
highmap.insert(0, ["#" for i in range(len(highmap[0]))])
highmap.append(["#" for i in range(len(highmap[0]))])
def coord(x, y):
    return str(x) + "," + str(y)
def decoord(xy):
    return list(map(int, xy.split(",")))
graph = {}
start = ""
finish = ""
for y in range(1, len(highmap) - 1):
    for x in range(1, len(highmap[0]) - 1):
        if highmap[y][x] == "S":
            start = coord(x, y)
            highmap[y][x] = "a"
        if highmap[y][x] == "E":
            finish = coord(x, y)
            highmap[y][x] = "z"
for y in range(1, len(highmap) - 1):
    for x in range(1, len(highmap[0]) - 1):
        curheight = highmap[y][x]
        connections = []
        weights = []

        # up
        nexthigh = highmap[y - 1][x]
        if nexthigh != "#":
            res = ord(nexthigh) - ord(curheight)
            if res <= 1:
                res = 1
                connections.append(coord(x, y - 1))
        
        # down
        nexthigh = highmap[y + 1][x]
        if nexthigh != "#":
            res = ord(nexthigh) - ord(curheight)
            if res <= 1:
                res = 1
                connections.append(coord(x, y + 1))

        # right
        nexthigh = highmap[y][x + 1]
        if nexthigh != "#":
            res = ord(nexthigh) - ord(curheight)
            if res <= 1:
                res = 1
                connections.append(coord(x + 1, y))

        # left
        nexthigh = highmap[y][x - 1]
        if nexthigh != "#":
            res = ord(nexthigh) - ord(curheight)
            if res <= 1:
                res = 1
                connections.append(coord(x - 1, y))

        graph[coord(x, y)] = connections
def takeOf(q):
    min = INF
    minCoord = ""
    for i in range(len(q)):
        if d[q[i]] <= min:
            min = d[q[i]]
            minCoord = q[i]
    q.remove(minCoord)
    return minCoord

d = {}
prevs = {}
for v in graph:
    d[v] = INF
    prevs[v] = "#,#"
d[start] = 0
q = []
for v in graph:
    q.append(v)
while len(q) > 0:
    u = takeOf(q)
    for v in graph[u]:
        if d[v] > d[u] + 1:
            d[v] = d[u] + 1
            prevs[v] = u
print("Shortest path:", d[finish])