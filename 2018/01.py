import re
left_start = []
top_start = []
width = []
height = []
ids = []
n = 0
# inputting
while True:
    try:
        num_claim = input()
    except EOFError:
        break
    # 1411 @ 120,917: 19x14
    match = re.search(r"(\d+) @ (\d+),(\d+): (\d+)x(\d+)", num_claim)
    ids.append(int(match.group(1)))
    left_start.append(int(match.group(2)))
    top_start.append(int(match.group(3)))
    width.append(int(match.group(4)))
    height.append(int(match.group(5)))
    n += 1

# drawing empty canvas
canvas = [[0 for i in range(1001)] for i in range(1001)]

# filling canvas with claims
frags1 = 0
i = 0
for id in ids:
    print(id, i)
    wd = width[i]
    hg = height[i]
    lf = left_start[i]
    tp = top_start[i]
    for j in range(hg):
        for k in range(wd):
            # print(tp+hg, lf+wd)
            if canvas[tp + j][lf + k] > 0:
                canvas[tp + j][lf + k] = -1
                frags1 += 1
            elif canvas[tp + j][lf + k] == 0:
                canvas[tp + j][lf + k] = 1
    i += 1

# counting multi-claimed fragments
frags2 = 0
for i in canvas:
    for j in i:
        if j == -1:
            frags2 += 1
# print(canvas)
print(frags1, frags2)