import math
seats = []

while True:
    try:
        ins = list(input())
    except EOFError:
        break
    insr = ins[:7]
    insc = ins[7:]
    print(insr)
    print(insc)

    row = (0, 127)
    for i in insr:
        mid = math.ceil((row[1] - row[0]) / 2)
        if i == "F":
            row = (row[0], row[1] - mid)
        elif i == "B":
            row = (row[0] + mid, row[1])
    rowint = row[0]

    col = (0, 7)
    for i in insc:
        mid = math.ceil((col[1] - col[0]) / 2)
        if i == "L":
            col = (col[0], col[1] - mid)
        elif i == "R":
            col = (col[0] + mid, col[1])
    colint = col[0]
    seats.append(rowint * 8 + colint)

seats.sort()
print(seats)
for i in range(1, len(seats)):
    if seats[i] - seats[i - 1] == 2:
        print(seats[i])
