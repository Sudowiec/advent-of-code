from collections import defaultdict
import copy

connections = defaultdict(lambda : [])
while True:
    try:
        inp = input().split("-")
    except EOFError:
        break
    connections[inp[0]].append(inp[1])
    connections[inp[1]].append(inp[0])
print(connections)

counter = 0
def dfs(point, bt):
    global counter
    if point == "end":
        counter += 1
        return
    to_go = connections[point]
    for i in to_go:
        if i in bt:
            continue
        if str.islower(i) and i != "end":
            dfs(i, bt.append(i))
        else:
            dfs(i, bt)
dfs("start", ["start"])
print(counter)