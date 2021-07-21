
inp = "19,20,14,0,9,1"
inp = inp.split(",")
inp = list(map(int, inp))
print(inp)

saidnums = {}

minus = 0
for i, k in enumerate(inp):
    saidnums[k] = i
    print(i, k)
    minus = i

p = 0
for i in range(minus + 1, 30000000 - 1):
    if i % 100000 == 0:
        print(i, p)
    if p in saidnums:
        d = i - saidnums[p]
    else:
        d = 0

    saidnums[p] = i
    p = d
print(p)



