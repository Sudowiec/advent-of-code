FILE_NAME = "2016/07.txt"
FILE_SIZE = 2000

def is_aba(potential_string):
    if potential_string[0] == potential_string[2] and potential_string[0] != potential_string[1]:
        return True
    return False

def check_aba_match(word_one, word_two):
    if word_one[0] == word_two[1] and word_two[1] == word_one[2]:
        if word_two[0] == word_one[1] and word_one[1] == word_two[2]:
            return True
    return False

count = 0
f = open(FILE_NAME)
for line_number in range(FILE_SIZE):
    full_line = f.readline().strip().replace("]", "[").split("[")
    outside_brackets = full_line[::2]
    outside_abas = []
    inside_brackets = full_line[1::2]
    inside_abas = []
    for word in outside_brackets:
        for i in range(0, len(word) - 2):
            if is_aba(word[i:i + 3]):
                outside_abas.append(word[i:i + 3])
    for word in inside_brackets:
        for i in range(0, len(word) - 2):
            if is_aba(word[i:i + 3]):
                inside_abas.append(word[i:i + 3])
    found_match = False
    for outside_word in outside_abas:
        for inside_word in inside_abas:
            if check_aba_match(outside_word, inside_word):
                found_match = True
        if found_match:
            break
    if found_match:
        count += 1
print(count)