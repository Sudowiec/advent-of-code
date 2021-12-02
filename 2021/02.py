hor = 0
dept = 0

while True:
    try:
        inp = input().split(" ")
    except EOFError:
        break

    if inp[0] == "down":
        dept += int(inp[1])
    elif inp[0] == "up":
        dept -= int(inp[1])
    elif inp[0] == "forward":
        hor += int(inp[1])
print(hor*dept)