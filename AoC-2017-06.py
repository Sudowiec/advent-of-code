inp = "0 5 10 0 11 14 13 4 11 8 8 7 1 4 12 11"
cache = {}
# inp = "0 2 7 0"
inp = list(map(int, inp.split(" ")))
length = len(inp)
print(inp)

indx = 1
while True:
    # find the highest
    h = max(inp)
    pos = inp.index(h)
    inp[pos] = 0
    # spread the highest
    for i in range(h):
        inp[(pos + i + 1) % length] += 1
    print(inp)
    # cache check
    strinp = "|".join(list(map(str, inp)))
    if strinp in cache:
        print(indx - cache[strinp])
        exit(0)
    else:
        cache[strinp] = indx
    indx += 1