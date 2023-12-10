import os, sys

LENGTH = 140

f = open(os.path.join(sys.path[0], "10.txt"), "r")

matrix = []

for i in range(LENGTH):
    matrix.append(list(f.readline().strip()))

graph = {}
start = []

for y in range(len(matrix)):
    for x in range(len(matrix[0])):
        curtile = matrix[y][x]
        if curtile == ".":
            continue
        elif curtile == "|":
            graph[str(x) + "," + str(y)] = [[x, y - 1],[x, y + 1]]
        elif curtile == "-":
            graph[str(x) + "," + str(y)] = [[x - 1, y],[x + 1, y]]
        elif curtile == "L":
            graph[str(x) + "," + str(y)] = [[x, y - 1],[x + 1, y]]
        elif curtile == "J":
            graph[str(x) + "," + str(y)] = [[x, y - 1],[x - 1, y]]
        elif curtile == "F":
            graph[str(x) + "," + str(y)] = [[x, y + 1],[x + 1, y]]
        elif curtile == "7":
            graph[str(x) + "," + str(y)] = [[x, y + 1],[x - 1, y]]
        elif curtile == "S": # ostrożnie
            start = [x, y]
            u = matrix[y - 1][x]
            d = matrix[y + 1][x]
            l = matrix[y][x - 1]
            r = matrix[y][x + 1]
            if u != ".":
                if d != ".":
                    graph[str(x) + "," + str(y)] = [[x, y - 1],[x, y + 1]]
                elif r != ".":
                    graph[str(x) + "," + str(y)] = [[x, y - 1],[x + 1, y]]
                elif l != ".":
                    graph[str(x) + "," + str(y)] = [[x, y - 1],[x - 1, y]]
            elif d != ".":
                if r != ".":
                    graph[str(x) + "," + str(y)] = [[x, y + 1],[x + 1, y]]
                elif l != ".":
                    graph[str(x) + "," + str(y)] = [[x, y + 1],[x - 1, y]]
            elif r == "." and l == ".":
                graph[str(x) + "," + str(y)] = [[x - 1, y],[x + 1, y]]

print(graph)

INF = 999999999
dist = {}
prev = {}
q = []
beento = []
for i in graph:
    dist[i] = INF
    prev[i] = -1
    q.append(i)
dist[str(start[0]) + "," + str(start[1])] = 0

def takeShortest():
    global q
    u = "x"
    length = INF
    for i in q:
        if dist[i] < length:
            length = dist[i]
            u = i
    return u

while len(q) > 0:
    u = takeShortest()
    if u == "x":
        break
    q.remove(u)
    beento.append(u)

    alt = dist[u] + 1
    for i in graph[u]:
        mock = str(i[0]) + "," + str(i[1]) #60, 101 | 61, 102
        if mock in beento:
            continue
        if alt < dist[mock]:
            dist[mock] = alt
            prev[mock] = u

print(dist)

s = 0
for i in dist:
    if dist[i] != INF and dist[i] > s:
        s = dist[i]
print(s)