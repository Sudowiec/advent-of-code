inp = input()
for i in range(13, len(inp)):
    if len(set(inp[i - 14 : i])) == 14:
        print(i)
        break