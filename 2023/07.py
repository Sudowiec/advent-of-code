import os, sys
from collections import defaultdict

f = open(os.path.join(sys.path[0], "07.txt"), "r")
LENGTH = 1000
HANDSIZE = 5
HIERARCHY = "J23456789TQKA"

handvals = {}
hands = []
for i in range(LENGTH):
    inp = f.readline().strip().split(" ")
    handvals[inp[0]] = int(inp[1])
    hands.append(inp[0])

def getHandName(hand):
    s = defaultdict(lambda : 0)
    for i in hand:
        s[i] += 1
    if s["J"] == 0:
        if len(s) - 1 == 5:
            return 1
        elif len(s) - 1 == 4:
            return 2
        elif len(s) - 1 == 3:
            if 3 not in s.values():
                return 3
            return 4
        elif len(s) - 1 == 2:
            if 4 not in s.values():
                return 5
            return 6
        elif len(s) - 1 == 1:
            return 7
    elif s["J"] == 1:
        if len(s) == 5:
            return 2
        elif len(s) == 4:
            return 4
        elif len(s) == 3:
            if 3 not in s.values():
                return 5
            return 6
        elif len(s) == 2:
            return 7
    elif s["J"] == 2:
        if len(s) == 4:
            return 4
        elif len(s) == 3:
            return 6
        elif len(s) == 2:
            return 7
    elif s["J"] == 3:
        if len(s) == 3:
            return 6
        elif len(s) == 2:
            return 7
    else:
        return 7


def compare(handOne, handTwo):
    if getHandName(handOne) == getHandName(handTwo):
        for i in range(HANDSIZE):
            vone = HIERARCHY.index(handOne[i])
            vtwo = HIERARCHY.index(handTwo[i])
            if vone > vtwo:
                return 1
            elif vone < vtwo:
                return -1
    elif getHandName(handOne) > getHandName(handTwo):
        return 1
    else:
        return -1

def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if compare(x, pivot) == -1]
        right = [x for x in arr[1:] if compare(x, pivot) == 1]
        return qsort(left) + [pivot] + qsort(right)

hands = qsort(hands)

total = 0
for i in range(LENGTH):
    total += (i + 1) * handvals[hands[i]]
print(total)