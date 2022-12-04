s = 0
while True:
    try:
        inp = input().split(",")
    except EOFError:
        break
    first = list(map(int, inp[0].split("-")))
    second = list(map(int, inp[1].split("-")))
    s += 1 if (first[0] >= second[0] and first[1] <= second[1]) or (second[0] >= first[0] and second[1] <= first[1]) else 0
print(s)