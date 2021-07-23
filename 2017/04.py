counter = 0
while True:
    try:
        inp = input().split(" ")
    except EOFError:
        break
    # ///STAGE 1///
    #
    # setinp = set(inp)
    # if len(setinp) == len(inp):
    #     counter += 1

    valid = True
    for i in range(len(inp)):
        for j in range(i, len(inp)):
            if i == j:
                continue
            listone = sorted(list(inp[i]))
            listtwo = sorted(list(inp[j]))
            if listone == listtwo:
                valid = False
                break
    if valid:
        counter += 1
print(counter)