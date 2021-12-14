import copy
ITER = 2
hx = 0
hy = 0
coords = []
while True:
    inp = input().split(",")
    if inp == [""]:
        break
    inp = list(map(int, inp))
    coords.append(inp)
    if inp[0] > hx:
        hx = inp[0]
    if inp[1] > hy:
        hy = inp[1]
page = [["." for j in range(hx + 1)] for i in range(hy + 1)]
for i in coords:
    page[i[1]][i[0]] = "#"

indx = 0
while True:
    if indx == ITER:
        break
    try:
        fold = input().split(" ")[2]
    except EOFError:
        break
    foldval = int(fold[2:])
    if fold[0] == "x":
        newpage = [["." for j in range(foldval)] for i in range(hy + 1)]
        for y in range(len(page)):
            for x in range(len(page[y])):
                if x > foldval and page[y][x] == "#":
                    newpage[y][2 * foldval - x] = "#"
    else:
        newpage = [["." for j in range(hx + 1)] for i in range(foldval)]
        for y in range(len(page)):
            for x in range(len(page[y])):
                if y > foldval and page[y][x] == "#":
                    newpage[2 * foldval - y][x] = "#"
    page = copy.deepcopy(newpage)
    indx += 1
print(hx, hy)
counter = 0
for i in page:
    print("".join(i))
    counter += i.count("#")
print(counter)


