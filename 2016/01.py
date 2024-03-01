f = open("2016/01.txt")
inp = f.readline().split(", ")
distance = 0
sides = ["N", "E", "S", "W"]
trans = {"L" : -1, "R" : 1}
curind = 0
pos = {"x" : 0, "y" : 0}
cache = []
for i in inp:
    curind = (curind + trans[i[0]]) % 4
    for j in range(int(i[1:])):
        if sides[curind] == "N":
            pos["y"] += 1
        elif sides[curind] == "S":
            pos["y"] -= 1
        elif sides[curind] == "E":
            pos["x"] += 1
        else:
            pos["x"] -= 1
        key = "x:" + str(pos["x"]) + "y:" + str(pos["y"])
        print(key)
        if key in cache:
            print(abs(pos["x"]) + abs(pos["y"]))
            exit()
        cache.append(key)
print("Not found")