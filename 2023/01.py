import os, sys

PATTERN = {"one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9"}
NUMBERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

s = 0
f = open(os.path.join(sys.path[0], "01.txt"), "r")
while True:
    l = f.readline().strip()
    if l == "":
        break
    nums = {}
    for i in PATTERN:
        found = list(find_all(l, i))
        for j in found:
            nums[j] = PATTERN[i]
    for i in NUMBERS:
        found = list(find_all(l, i))
        for j in found:
            nums[j] = i
    num = int(nums[min(nums.keys())] + nums[max(nums.keys())])
    s += num
print(s)