from collections import defaultdict
SQUARE = 25
carrierpos = "0,0"
carrierdir = "u"
grid = defaultdict(lambda : ".")
right = {"r" : "d", "d" : "l", "l" : "u", "u" : "r"}
left = {"r" : "u", "d" : "r", "l" : "d", "u" : "l"}
reverse = {"r" : "l", "d" : "u", "l" : "r", "u" : "d"}

# init
counter = 0
y = -(SQUARE // 2)
while True:
    try:
        inp = list(input())
    except EOFError:
        break
    x = -(SQUARE // 2)
    for i in range(SQUARE):
        grid[str(x) + "," + str(y)] = inp[i]
        x += 1
    y += 1

# main loop
for time in range(10000000):
    # turn the carrier
    if grid[carrierpos] == "#":
        carrierdir = right[carrierdir]
    elif grid[carrierpos] == ".":
        carrierdir = left[carrierdir]
    elif grid[carrierpos] == "F":
        carrierdir = reverse[carrierdir]

    # infecting / cleaning / flagging / weakening
    if grid[carrierpos] == ".":
        grid[carrierpos] = "W"
    elif grid[carrierpos] == "W":
        grid[carrierpos] = "#"
        counter += 1
    elif grid[carrierpos] == "#":
        grid[carrierpos] = "F"
    elif grid[carrierpos] == "F":
        grid[carrierpos] = "."

    # move the carrier
    x = int(carrierpos.split(",")[0])
    y = int(carrierpos.split(",")[1])
    if carrierdir == "u":
        y -= 1
    elif carrierdir == "d":
        y += 1
    elif carrierdir == "r":
        x += 1
    elif carrierdir == "l":
        x -= 1
    carrierpos = str(x) + "," + str(y)
print(counter)

