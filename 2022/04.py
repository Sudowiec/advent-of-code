s = 0
while True:
    try:
        inp = input().split(",")
    except EOFError:
        break
    first = list(map(int, inp[0].split("-")))
    second = list(map(int, inp[1].split("-")))
    arr = []
    for i in range(first[0], first[1] + 1):
        arr.append(i)
    for i in range(second[0], second[1] + 1):
        arr.append(i)
    setArr = set(arr)
    s += 1 if len(setArr) < len(arr) else 0
print(s)