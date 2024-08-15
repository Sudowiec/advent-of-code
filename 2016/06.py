from collections import defaultdict
import sys, time

FILE_NAME = "2016/06.txt"
FILE_LENGTH = 650
PART_ONE = False

input_matrix = []
f = open(FILE_NAME)
for i in range(FILE_LENGTH):
    input_matrix.append(list(f.readline().strip()))

password = ["-" for i in range(len(input_matrix[0]))]
for x in range(len(input_matrix[0])):
    letter_ranks = defaultdict(lambda : 0)
    for y in range(len(input_matrix)):
        time.sleep(0.001)
        current_letter = input_matrix[y][x]
        letter_ranks[current_letter] += 1
        chosen_letter = ""
        if PART_ONE:
            chosen_presence = 0
            for letter in letter_ranks:
                if letter_ranks[letter] > chosen_presence:
                    chosen_presence = letter_ranks[letter]
                    chosen_letter = letter
        else:
            chosen_presence = 99999999
            for letter in letter_ranks:
                if letter_ranks[letter] < chosen_presence:
                    chosen_presence = letter_ranks[letter]
                    chosen_letter = letter
        password[x] = chosen_letter
        sys.stdout.write("\r" + "".join(password))

