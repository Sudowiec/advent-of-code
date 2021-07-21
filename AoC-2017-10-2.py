# initialize
STRINGLENTH = 256
INP = "a0c2017"
lengths = list(INP)
for i in range(len(lengths)):
    lengths[i] = ord(lengths[i])
lengths.extend([17, 31, 73, 47, 23])
print(lengths)
nums = []
for i in range(STRINGLENTH):
    nums.append(i)
print(nums)

# sparse hash
skip = 0
pos = 0
for time in range(64):
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

# dense hash
densehash = []
tohash = []
for i in range(16):
    tohash.append(nums[i*16:((i+1)*16)])
print(tohash)
for i in tohash:
    num = i[0]
    for j in range(1, len(i)):
        num = num ^ i[j]
    densehash.append(num)
print(densehash)

# hex
hexhash = ""
for i in range(len(densehash)):
    hexy = hex(densehash[i])
    hexy = hexy[2:]
    if len(hexy) < 2:
        hexy = '0' + hexy
    hexhash += hexy
print(hexhash)
