slope = []
while True:
    try:
        inp = input()
    except EOFError:
        break
    slope.append(list(inp))
height = len(slope)
length = len(slope[0])
print(height)
slopestulp = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

treesmul = 1

for i in slopestulp:
    trees = 0
    x = 0
    y = 0
    while y < height:
        if slope[y][x] == '#':
            trees += 1
        y += i[1]
        x = (x + i[0]) % length
    print(trees)
    treesmul *= trees
print(treesmul)