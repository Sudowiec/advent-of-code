import os, sys

f = open(os.path.join(sys.path[0], "06.txt"), "r")

times = list(map(int, list(filter(("").__ne__, f.readline().strip().split(" ")))[1:]))
distances = list(map(int, list(filter(("").__ne__, f.readline().strip().split(" ")))[1:]))

m = 1
for t in range(len(times)):
    curtime = times[t]
    curdistance = distances[t]
    s = 0
    for bvel in range(curtime + 1):
        print(bvel)
        distance = (curtime - bvel) * bvel
        if distance > curdistance:
            s += 1
    m *= s
print(m)
