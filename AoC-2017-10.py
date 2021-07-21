# initialize
STRINGLENTH = 256
INP = "94,84,0,79,2,27,81,1,123,93,218,23,103,255,254,243"
lengths = list(map(int, INP.split(",")))
nums = []
for i in range(STRINGLENTH):
    nums.append(i)
print(nums)

skip = 0
pos = 0
for currlen in lengths:
    # reverse
    torev = []
    for i in range(currlen):
        torev.append(nums[(pos+i) % STRINGLENTH])
    torev.reverse()
    for i in range(currlen):
        nums[(pos+i) % STRINGLENTH] = torev[i]
    # move
    pos += (currlen + skip) % STRINGLENTH
    # increase
    skip += 1
    print(nums)
print(nums[0]*nums[1])