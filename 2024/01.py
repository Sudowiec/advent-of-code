FILE_NAME = "2024/01.txt"
FILE_SIZE = 1000
PART = 2

left = []
right = []
f = open(FILE_NAME, "r")
for line_number in range(FILE_SIZE):
    pair = list(map(int, f.readline().split("   ")))
    left.append(pair[0])
    right.append(pair[1])

if PART == 1:
    sum_distance = 0
    while len(left) > 0:
        smallest_left = left.pop(left.index(min(left)))
        smallest_right = right.pop(right.index(min(right)))
        distance = abs(smallest_left - smallest_right)
        sum_distance += distance
    print(f"Part 1: {sum_distance}")
else:
    similarity_score = 0
    cache = {}
    for left_number in left:
        if left_number in cache:
            similarity_score += cache[left_number]
            continue
        multiplicator = 0
        for right_number in right:
            if left_number == right_number:
                multiplicator += 1
        result = left_number * multiplicator
        similarity_score += result
        cache[left_number] = result
    print(f"Part 2: {similarity_score}")