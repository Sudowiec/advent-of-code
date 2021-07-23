back = 25
inps = []

while True:
    try:
        inps.append(int(input()))
    except EOFError:
        break

for pos in range(back, len(inps) + 1):
    posnums = []
    for j in range(1, back + 1):
        posnums.append(inps[pos - j])
    # print(posnums)
    lfnum = inps[pos]
    valid = False
    for j in posnums:
        test = lfnum - j
        if (test) in posnums:
            valid = True
            break
    if not valid:
        print(lfnum)
        break
# 530627549

length = 2

i = 0
j = 1
crock_sum = inps[i] + inps[j]
while True:
    if crock_sum == lfnum:
        print(crock_sum)
        break
    elif crock_sum < lfnum:
        j += 1
        crock_sum += inps[j]
    elif crock_sum > lfnum:
        crock_sum -= inps[i]
        i += 1

while length <= len(inps):
    subs = []
    sub = []
    index = 0
    while index < len(inps):
        sub.append(inps[index])
        if len(sub) % length == 0:
            subs.append(sub)
            index -= len(sub) - 1
            sub = []
        index += 1

    for i in subs:
        if sum(i) == lfnum:
            print(max(i), min(i), len(i))


    length += 1

