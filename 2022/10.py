f = open("2022/10.txt")
stack = []
while True:
    cmd = f.readline().strip()
    if cmd == "":
        break
    if (cmd == "noop"):
        stack.append(cmd)
    else:
        stack.append("noop")
        stack.append(cmd)
x = 1
s = 0
for i in range(len(stack)):
    if stack[i] == "noop":
        if not ((i - 19) % 40):
            s += (i + 1) * x
        continue
    else:
        if not ((i - 19) % 40):
            s += (i + 1) * x
        x += int(stack[i].split(" ")[1])
print("Sum:", s)

# Part 2
x = 1
screen = []
curRow = []
for i in range(len(stack)):
    curPos = i % 40
    if stack[i] == "noop":
        plus = 0
    else:
        plus = int(stack[i].split(" ")[1])
    if (curPos == x - 1) or (curPos == x) or (curPos == x + 1):
        curRow.append("#")
    else:
        curRow.append(".")
    if len(curRow) == 40:
        screen.append(curRow)
        curRow = []
    x += plus
for i in screen:
    print("".join(i))