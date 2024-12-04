FILE_NAME = "2024/04.txt"
FILE_LENGTH = 140

def print_matrix(matrix):
    for i in matrix:
        print("".join(i))

CHECK_PATTERN = ["UL", "U", "UR", "DL", "D", "DR", "L", "R"]
def check_for_m(matrix, x, y):
    checklist = []
    checklist.extend(matrix[y - 1][x - 1 : x + 2])
    checklist.extend(matrix[y + 1][x - 1 : x + 2])
    checklist.append(matrix[y][x - 1])
    checklist.append(matrix[y][x + 1])
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

sum = 0
for y in range(len(matrix)):
    for x in range(len(matrix[0])):
        if matrix[y][x] != "X":
            continue
        directions = check_for_m(matrix, x, y)
        for direction in directions:
            cx,cy = setup_changes_for_coords(direction)
            if matrix[y + (cy * 2)][x + (cx * 2)] == "A":
                if matrix[y + (cy * 3)][x + cx * 3] == "S":
                    sum += 1
print(sum)
