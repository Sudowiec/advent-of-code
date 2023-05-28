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
            print(i + 1, x)
            s += (i + 1) * x
        continue
    else:
        if not ((i - 19) % 40):
            print(i + 1, x)
            s += (i + 1) * x
        x += int(stack[i].split(" ")[1])
print(s)