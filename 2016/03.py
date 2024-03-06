FLENGTH = 1914
f = open("2016/03.txt")
count = 0

for i in range(0, FLENGTH, 3):
    rows = []
    for j in range(3):
        rows.append(list(map(int, filter(lambda a: a != "", f.readline().strip().split(" ")))))
    for r in range(3):
        l = []
        for k in range(3):
            l.append(rows[k][r])
        c = l.pop(l.index(max(l)))
        if sum(l) > c:
            count += 1
print(count)