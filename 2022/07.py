from collections import defaultdict
inp = open("2022/07.txt", "r")
inp.readline()
weights = {}

dirstack = ["~"]
while True:
    cmd = inp.readline()[:-1]
    if not cmd:
        break
    if cmd[0] == "$":
        if cmd[2:4] == "cd":
            if cmd[5:7] == "..":
                dirstack.pop()
            else:
                dirstack.append(cmd[5:])
                pth = "/".join(dirstack) + "/"
                weights[pth] = 0
    else:
        if not cmd.split(" ")[0] == "dir":
            pth = "/".join(dirstack) + "/" + cmd.split(" ")[1]
            weights[pth] = int(cmd.split(" ")[0])
dirweights = defaultdict(lambda : 0)
for i in weights:
    tc = i.split("/")
    tc.pop()
    dirweights["/".join(tc)] += weights[i]
for i in dirweights:
    for j in dirweights:
        if (i + "/") in j:
            dirweights[i] += dirweights[j]
s = 0
for i in dirweights:
    if dirweights[i] <= 100000:
        s += dirweights[i]
print("Part 1:", s)

todel = 30000000 - (70000000 - dirweights["~"])
print(todel)
num = 999999999
for i in dirweights:
    if dirweights[i] < num and dirweights[i] > todel:
        num = dirweights[i]
print("Part 2:", num)
