def printdisk(matrix):
    for i in matrix:
        print("".join(i))

def knothash(text):
    STRINGLENTH = 256
    lengths = list(text)
    for i in range(len(lengths)):
        lengths[i] = ord(lengths[i])
    lengths.extend([17, 31, 73, 47, 23])
    nums = []
    for i in range(STRINGLENTH):
        nums.append(i)
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
    # dense hash
    densehash = []
    tohash = []
    for i in range(16):
        tohash.append(nums[i*16:((i+1)*16)])
    for i in tohash:
        num = i[0]
        for j in range(1, len(i)):
            num = num ^ i[j]
        densehash.append(num)
    # hex
    hexhash = ""
    for i in range(len(densehash)):
        hexy = hex(densehash[i])
        hexy = hexy[2:]
        if len(hexy) < 2:
            hexy = '0' + hexy
        hexhash += hexy
    return(hexhash)

disk = []
inp = "ffayrhll"
for number in range(128):
    tohash = inp + "-" + str(number)
    tohash = knothash(tohash)
    binhash = []
    for i in list(tohash):
        binary = bin(int(i, 16))[2:]
        if len(binary) < 4:
            for i in range(4 - len(binary)):
                binary = '0' + binary
        binhash.append(binary)
    binhash = "".join(binhash)
    print(tohash)
    print(binhash)
    binhash = list(binhash)
    for i in range(len(binhash)):
        if binhash[i] == '0':
            binhash[i] = "."
        else:
            binhash[i] = "#"
    binhash.append("-")
    binhash.insert(0, "-")
    disk.append(binhash)

index = 0
disk.append(["-" for i in range(130)])
disk.insert(0, ["-" for i in range(130)])
for prey in range(1, 129):
    for prex in range(1, 129):
        que = [[prey, prex]]
        if disk[prey][prex] == "#":
            index += 1
        while len(que) > 0:
            pair = que.pop(0)
            y = pair[0]
            x = pair[1]
            if disk[y][x] == "#":
                disk[y][x] = str(index)
                if disk[y-1][x] == "#":
                    que.append([y-1, x])
                if disk[y+1][x] == "#":
                    que.append([y+1, x])
                if disk[y][x-1] == "#":
                    que.append([y, x-1])
                if disk[y][x+1] == "#":
                    que.append([y, x+1])
printdisk(disk)
print(index)



