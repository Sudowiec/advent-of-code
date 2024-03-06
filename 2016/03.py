FLENGTH = 1914
f = open("2016/03.txt")
count = 0

for i in range(FLENGTH):
    l = list(map(int, filter(lambda a: a != "", f.readline().strip().split(" "))))
    c = l.pop(l.index(max(l)))
    if sum(l) > c:
        count += 1
print(count)