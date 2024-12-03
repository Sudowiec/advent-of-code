FILE_NAME = "2024/01.txt"
FILE_SIZE = 1000

left = []
right = []
f = open(FILE_NAME, "r")
for line_number in range(FILE_SIZE):
    pair = list(map(int, f.readline().split("   ")))
    left.append(pair[0])
    right.append(pair[1])

sum_distance = 0
while len(left) > 0:
    smallest_left = left.pop(left.index(min(left)))
    smallest_right = right.pop(right.index(min(right)))
    distance = abs(smallest_left - smallest_right)
    sum_distance += distance

print(sum_distance)