import sys, os, time

FILE_NAME = "2024/04.txt"
FILE_LENGTH = 140
PART = 2

COL_RESET = "\033[0;0m"
COL_GREY = "\033[2;37m"
COL_GREEN = "\033[0;32m"
CURSOR_UP = "\033[F"

def print_matrix(matrix, fin = False):
    to_print = f"{COL_GREY}"
    for row in range(1, len(matrix) - 1):
        to_print += ("".join(matrix[row][1:-1]) + "\n")
    if not fin:
        to_print += "".join([CURSOR_UP for i in range(len(matrix))])
    sys.stdout.write(to_print)

def get_around(matrix, x, y):
    around = []
    around.extend(matrix[y - 1][x - 1 : x + 2])
    around.extend(matrix[y + 1][x - 1 : x + 2])
    around.append(matrix[y][x - 1])
    around.append(matrix[y][x + 1])
    return around

CHECK_PATTERN = ["UL", "U", "UR", "DL", "D", "DR", "L", "R"]
def check_for_m(matrix, x, y):
    checklist = get_around(matrix, x, y)
    indices = [i for i, x in enumerate(checklist) if x == "M"]
    return [CHECK_PATTERN[i] for i in indices]

def setup_changes_for_coords(direction):
    if "L" in direction:
        change_x = -1
    elif "R" in direction:
        change_x = 1
    else:
        change_x = 0
    if "U" in direction:
        change_y = -1
    elif "D" in direction:
        change_y = 1
    else:
        change_y = 0
    return change_x, change_y

matrix = []
f = open(FILE_NAME, "r")
for line_number in range(FILE_LENGTH):
    matrix.append(list(f"#{f.readline().strip()}#"))
matrix.insert(0, ["#" for i in range(len(matrix[0]))])
matrix.append(["#" for i in range(len(matrix[0]))])

os.system("cls")
sum = 0
to_print = []
X_MAS_PATTERN = ["MSMS", "MMSS", "SMSM", "SSMM"]
for y in range(len(matrix)):
    for x in range(len(matrix[0])):
        if PART == 1:
            if matrix[y][x] != "X":
                continue
            directions = check_for_m(matrix, x, y)
            for direction in directions:
                cx,cy = setup_changes_for_coords(direction)
                if matrix[y + (cy * 2)][x + (cx * 2)] == "A":
                    if matrix[y + (cy * 3)][x + cx * 3] == "S":
                        for i in range(4):
                            matrix[y + (cy * i)][x + (cx * i)] = f"{COL_GREEN}{matrix[y + (cy * i)][x + (cx * i)]}{COL_GREY}"
                        print_matrix(matrix)
                        sum += 1
        else:
            if matrix[y][x] != "A":
                continue
            around = "".join([get_around(matrix, x, y)[i] for i in [0, 2, 3, 5]])
            if around in X_MAS_PATTERN:
                matrix[y][x] = f"{COL_GREEN}{matrix[y][x]}{COL_GREY}"
                for cy in [-1, 1]:
                    for cx in [-1, 1]:
                        matrix[y + cy][x + cx] = f"{COL_GREEN}{matrix[y + cy][x + cx]}{COL_GREY}"
                print_matrix(matrix)
                sum += 1
print_matrix(matrix, True)
print(f"{COL_RESET}SUM: {COL_GREEN}{sum}")