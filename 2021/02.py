hor = 0
dept = 0
aim = 0

while True:
    try:
        inp = input().split(" ")
    except EOFError:
        break

    if inp[0] == "down":
        aim += int(inp[1])
    elif inp[0] == "up":
        aim -= int(inp[1])
    elif inp[0] == "forward":
        hor += int(inp[1])
        dept += int(inp[1]) * aim
    print(hor, dept, aim)
print(hor*dept)