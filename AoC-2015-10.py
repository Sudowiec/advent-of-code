import re
num = int(input())
print(num)
strnum = str(num)
for i in range(50):
    # 132123222113
    newnum = []
    counter = 0
    lnum = ''
    indx = 0
    for j in strnum:
        if j != lnum and indx > 0:
            newnum.append(str(counter))
            newnum.append(lnum)
            counter = 0
        counter += 1
        lnum = j
        indx += 1
    newnum.append(str(counter))
    newnum.append(lnum)
    strnum = ''.join(newnum)
# print(num)
print(len(strnum))

def conway(m):
    return str(len(m.group(1))) + str(m.group(2))

strnum = str(num)
for i in range(50):
    strnum = re.sub(r"((\d)\2*)", conway, strnum)
print(len(strnum))