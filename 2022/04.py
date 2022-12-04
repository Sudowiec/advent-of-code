s = 0
while True:
    try:
        inp = input().split(",")
    except EOFError:
        break
    arr = []
    arr.extend(range(int(inp[0].split("-")[0]), int(inp[0].split("-")[1]) + 1))
    arr.extend(range(int(inp[1].split("-")[0]), int(inp[1].split("-")[1]) + 1))
    s += 1 if len(set(arr)) < len(arr) else 0
print(s)