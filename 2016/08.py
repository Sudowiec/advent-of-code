import sys, os, time

FILE_NAME = "2016/08.txt"
FILE_SIZE = 162
MATRIX_W = 50
MATRIX_H = 6
FULL_SIGN = "#"
EMPTY_SIGN = " "
SPEED = 0.001

matrix = [[EMPTY_SIGN for j in range(MATRIX_W)] for i in range(MATRIX_H)]

def print_matrix(fin = False):
    to_print = ""
    for row in matrix:
        to_print += ("".join(row) + "\n")
    if not fin:
        to_print += "".join(["\033[F" for i in range(MATRIX_H)])
    sys.stdout.write(to_print)

def rotate_row(coordinate):
    ending = matrix[coordinate].pop()
    to_insert = ending if ending == FULL_SIGN else EMPTY_SIGN
    matrix[coordinate].insert(0, to_insert)

def rotate_column(coordinate):
    cut_column = []
    for i in range(MATRIX_H):
        cut_column.append(matrix[i][coordinate])
    ending = cut_column.pop()
    to_insert = ending if ending == FULL_SIGN else EMPTY_SIGN
    cut_column.insert(0, to_insert)
    for i in range(MATRIX_H):
        matrix[i][coordinate] = cut_column[i]

f = open(FILE_NAME)
os.system("cls")
for line_number in range(FILE_SIZE):
    time.sleep(SPEED)
    instruction = f.readline().strip().split(" ")
    if instruction[0] == "rect":
        width_to_display = int(instruction[1].split("x")[0])
        height_to_display = int(instruction[1].split("x")[1])
        for y in range(height_to_display):
            for x in range(width_to_display):
                matrix[y][x] = FULL_SIGN
        print_matrix()
    elif instruction[0] == "rotate":
        coordinate = int(instruction[2].split("=")[1])
        movement = int(instruction[4])
        if instruction[1] == "row":
            for i in range(movement):
                rotate_row(coordinate)
                print_matrix()
        elif instruction[1] == "column":
            for i in range(movement):
                rotate_column(coordinate)
                print_matrix()
    else:
        exit()
print_matrix(True)
full_sum = 0
for i in matrix:
    full_sum += i.count(FULL_SIGN)
print(f"Lit: {full_sum}")