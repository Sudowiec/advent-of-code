COUNTED = 204
LAST = "T"
# matrix print
def printmat(matrix):
    for i in matrix:
        print("".join(i))

# diagram import
matrix = []
while True:
    try:
        pre = list(input())
        while len(pre) < COUNTED:
            pre.append(" ")
        pre.append("#")
        pre.insert(0, "#")
        matrix.append(pre)
    except EOFError:
        break

matrix.insert(0, (list("#" for i in range(len(matrix[0])))))
matrix.append(list("#" for i in range(len(matrix[len(matrix) - 1]))))

printmat(matrix)

# start point
x = 1
y = 1
dir = "down"
for i in range(len(matrix[0])):
    if matrix[y][i] == "|":
        x = i
print(x, y)

# moving
counter = 0
while True:
    # what is around the pointer
    on = matrix[y][x]
    up = matrix[y-1][x]
    down = matrix[y+1][x]
    left = matrix[y][x-1]
    right = matrix[y][x+1]

    if on == "+":
        if dir == "down" or dir == "up":
            if left == "#" or left == " ":
                dir = "right"
                x += 1
            elif right == "#" or right == " ":
                dir = "left"
                x -= 1
        elif dir == "left" or dir == "right":
            if up == "#" or up == " ":
                dir = "down"
                y += 1
            elif down == "#" or down == " ":
                dir = "up"
                y -= 1
    elif on == LAST:
        print(on)
        print(counter + 1)
        exit(0)
    else:
        if on != "|" and on != "-":
            print(on)
        if dir == "down":
            y += 1
        elif dir == "up":
            y -= 1
        elif dir == "left":
            x -= 1
        elif dir == "right":
            x += 1
    counter += 1
    # print(x, y)

