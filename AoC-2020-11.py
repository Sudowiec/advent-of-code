import copy
ogmatrix = []
while True:
    try:
        ogmatrix.append(list(input()))
    except EOFError:
        break

mathash = {}
while True:
    matrix = copy.deepcopy(ogmatrix)

    for i in matrix:
        i.insert(0, "-")
        i.append("-")
    matrix.insert(0, ["-" for i in range(len(matrix[1]))])
    matrix.append(["-" for i in range(len(matrix[1]))])
    # print(matrix)

    for y in range(1, len(matrix) - 1):
        for x in range(1, len(matrix[0]) - 1):

            if matrix[y][x] == '.':
                continue

            occhash = {"#" : 0, "L" : 0, "." : 0, "-" : 0}

            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    if dy == 0 and dx == 0:
                        continue
                    pluser = 1
                    while True:
                        occhash[matrix[y + pluser * dy][x + pluser * dx]] += 1
                        if matrix[y + pluser * dy][x + pluser * dx] != ".":
                            break
                        pluser += 1

            # print(vals)
            # if x == 1 and y == 2:
                # print(occhash)
            if occhash["#"] == 0 and matrix[y][x] == "L":
                ogmatrix[y - 1][x - 1] = "#"
            if occhash["#"] >= 5 and matrix[y][x] == "#":
                ogmatrix[y - 1][x - 1] = "L"

    matstr = ""
    for i in ogmatrix:
        matstr += "".join(i)

    if matstr in mathash:
        counter = 0
        for i in matstr:
            if i == "#":
                counter += 1
        print(counter)
        exit(0)
    else:
        mathash[matstr] = 1

    #print()
    #for i in ogmatrix:
        #print("".join(i))
