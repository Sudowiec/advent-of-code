import sys, itertools

FILE_NAME = "2016/21.txt"
FILE_LENGTH = 100
LOOKING_FOR = "fbgdceah"
PATTERN = "abcdefgh"

def swap(string, index_one, index_two):
    string = list(string)
    string[index_one], string[index_two] = string[index_two], string[index_one]
    return "".join(string)

def rotate(string, direction):
    string = list(string)
    if direction == "right":
        tmp = string.pop()
        string.insert(0, tmp)
    else:
        tmp = string.pop(0)
        string.append(tmp)
    return "".join(string)

def reverse(string, index_one, index_two):
    return string[:index_one] + string[index_one:index_two+1][::-1] + string[index_two+1:]

def move(string, index_one, index_two):
    string = list(string)
    tmp = string.pop(index_one)
    string.insert(index_two, tmp)
    return "".join(string)

perms = []
perms = list(itertools.permutations(list(PATTERN)))
for i in range(len(perms)):
    perms[i] = "".join(perms[i])

instructions = []
f = open(FILE_NAME)
for i in range(FILE_LENGTH):
    instructions.append(f.readline().strip().split(" "))

for p in perms:
    current_combination = p
    for instruction in instructions:
        if instruction[0] == "swap":
            if instruction[1] == "position":
                current_combination = swap(current_combination, int(instruction[2]), int(instruction[5]))
            else:
                current_combination = swap(current_combination, current_combination.index(instruction[2]), current_combination.index(instruction[5]))
        elif instruction[0] == "rotate":
            if instruction[1] == "based":
                times = current_combination.index(instruction[6]) + 1
                times += 1 if times > 4 else 0
                direction = "right"
            else:
                times = int(instruction[2])
                direction = instruction[1]
            for i in range(times):
                current_combination = rotate(current_combination, direction)
        elif instruction[0] == "reverse":
            current_combination = reverse(current_combination, int(instruction[2]), int(instruction[4]))
        elif instruction[0] == "move":
            current_combination = move(current_combination, int(instruction[2]), int(instruction[5]))
    if current_combination == LOOKING_FOR:
        print(p)
        break