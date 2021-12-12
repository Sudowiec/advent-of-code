# pattern I used:
#  1 1
# 2   3
# 2   3
#  4 4
# 5   6
# 5   6
#  7 7
pattern = {
    0 : "123567",
    1 : "36",
    2 : "13457",
    3 : "13467",
    4 : "2346",
    5 : "12467",
    6 : "124567",
    7 : "136",
    8 : "1234567",
    9 : "123467"
}
counter = 0
while True:
    try:
        maininp = input().split("|")
    except EOFError:
        break
    connections = {}

    inp = maininp[0].split(" ")
    inp.pop()
    outp = maininp[1].split(" ")
    outp.pop(0)

    # finding 1
    to_search = []
    for i in inp:
        if len(i) == 2:
            to_search.append(i)
    for i in inp:
        if len(i) == 3:
            to_search.append(i)
    for i in to_search[1]:
        if i not in to_search[0]:
            connections[1] = i

    # finding 2, 3, 4, 5, 6
    one = list(to_search[0])
    to_search = []
    for i in inp:
        if len(i) == 6:
            to_search.append(i)
        if len(i) == 4:
            four = i
    print(to_search)
    print(four)
    missing = []
    for i in to_search:
        for j in "abcdefg":
            if j not in i:
                missing.append(j)
    print(missing)
    for i in missing:
        if i in one:
            connections[3] = i
        if i in four and i not in one:
            connections[4] = i
        if i not in four and i not in one:
            connections[5] = i
    if one[0] == connections[3]:
        connections[6] = one[1]
    else:
        connections[6] = one[0]

    # finding 2, 7
    for i in four:
        if i not in connections.values():
            connections[2] = i
    for i in "abcdefg":
        if i not in connections.values():
            connections[7] = i
    print(connections)

    # making translator
    translator = {}
    for i in range(10):
        tt = pattern[i]
        to_post = []
        for j in tt:
            to_post.append(connections[int(j)])
        translator[i] = "".join(sorted(to_post))
    translator = {y : x for x, y in translator.items()}
    print(translator)

    # translating numbers
    num = ""
    for i in outp:
        num += str(translator["".join(sorted(i))])
    counter += int(num)
print(counter)