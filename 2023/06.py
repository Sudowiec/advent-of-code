import os, sys

f = open(os.path.join(sys.path[0], "06.txt"), "r")

times = list(map(int, list(filter(("").__ne__, f.readline().strip().split(" ")))[1:]))
distances = list(map(int, list(filter(("").__ne__, f.readline().strip().split(" ")))[1:]))

for t in range(len(times)):
    curtime = times[t]
    curdistance = distances[t]
    b = 0
    e = 0
    for bvel in range(curtime + 1):
        distance = (curtime - bvel) * bvel
        if distance > curdistance:
            b = bvel
            break
    e = curtime - b
    m = e - b + 1
print(m, b, e)