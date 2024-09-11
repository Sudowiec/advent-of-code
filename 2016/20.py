import sys

FILE_NAME = "2016/20.txt"
FILE_LENGTH = 1029

blacklists = []
f = open(FILE_NAME)
for i in range(FILE_LENGTH):
    blacklists.append(list(map(int, f.readline().strip().split("-"))))

lowest = 0
while True:
    found = True
    for r in blacklists:
        if r[0] <= lowest and r[1] > lowest:
            lowest = r[1] + 1
            found = False
            break
    if found:
        break
print(lowest)