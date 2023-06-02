f = open("2016/01.txt")
inp = f.readline().split(", ")
distance = 0
sides = ["N", "E", "S", "W"]
trans = {"L" : -1, "R" : 1}
curind = 0
for i in inp:
    curind = (curind + trans[i[0]]) % 4
    if sides[curind] == "N" or sides[curind] == "E":
        distance += int(i[1:])
    else:
        distance -= int(i[1:])
print(abs(distance))
