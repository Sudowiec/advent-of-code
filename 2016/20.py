import sys

FILE_NAME = "2016/20.txt"
FILE_LENGTH = 1029
MAXVAL = 4294967296

blacklists = []
f = open(FILE_NAME)
for i in range(FILE_LENGTH):
    blacklists.append(list(map(int, f.readline().strip().split("-"))))

lowest = 0
count = 0
while lowest < MAXVAL:
    found = True
    for r in blacklists:
        if r[0] <= lowest and r[1] > lowest:
            lowest = r[1] + 1
            found = False
            break
    if found:
        count += 1
        lowest += 1
print(count)