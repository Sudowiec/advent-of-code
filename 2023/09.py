import os, sys

LENGTH = 200
PART = 2

f = open(os.path.join(sys.path[0], "09.txt"), "r")

s = 0
for i in range(LENGTH):
    start = list(map(int, f.readline().strip().split(" ")))
    l = []
    cur = start
    while True:
        l.append(cur)
        if list(set(cur)) == [0]:
            break
        n = []
        for i in range(len(cur) - 1):
            n.append(cur[i + 1] - cur[i])
        cur = n
    print(l)
    curIndex = len(l) - 1
    if PART == 1:
        l[curIndex].append(0)
        while curIndex > 0:
            curIndex -= 1
            left = l[curIndex][len(l[curIndex]) - 1]
            down = l[curIndex + 1][len(l[curIndex]) - 1]
            l[curIndex].append(left + down)
        s += l[0][len(l[0]) - 1]
        print(l)
    elif PART == 2:
        l[curIndex].insert(0, 0)
        while curIndex > 0:
            curIndex -= 1
            right = l[curIndex][0]
            down = l[curIndex + 1][0]
            l[curIndex].insert(0, right - down)
        s += l[0][0]
        print(l)
print(s)
    