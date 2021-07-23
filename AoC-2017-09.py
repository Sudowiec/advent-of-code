import re
prevlen = 9999999
def f(mobj):
    mobjs = mobj.group(1)
    mobj_two = ""
    for i in mobjs:
        mobj_two += chr(ord(i) + 1)
    return("A" + mobj_two)

count = 0
def counter(mobj):
    global count
    mobjs = mobj.group(1)
    count += len(mobjs)
    return("")

inp = input()
inp = re.sub(r"!.", "", inp)
inp = re.sub(r"<([^>]*)>", counter, inp)
inp = re.sub(r"[^{}]+", "", inp)
print(inp)
lvl = 0
sumup_two = 0
for i in inp:
    if i == "{":
        lvl += 1
    else:
        sumup_two += lvl
        lvl -= 1

while len(inp) < prevlen:
    prevlen = len(inp)
    inp = re.sub(r"\{([A-Z]*)\}", f, inp)
print(inp)
sumup = 0
for i in inp:
    sumup += ord(i) - 64
print(sumup, count, sumup_two)


