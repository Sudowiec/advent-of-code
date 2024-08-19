FILE_NAME = "2016/07.txt"
FILE_SIZE = 2000

def is_abba(potential_string):
    if len(set(potential_string)) != 1:
        if potential_string[0:2] == "".join(reversed(potential_string[2:4])):
            return True
    return False

count = 0
f = open(FILE_NAME)
for line_number in range(FILE_SIZE):
    full_line = f.readline().strip().replace("]", "[").split("[")
    outside_brackets = full_line[::2]
    inside_brackets = full_line[1::2]
    tls_outside_brackets = False
    tls_inside_brackets = False
    for word in outside_brackets:
        for i in range(0, len(word) - 3):
            if is_abba(word[i:i + 4]):
                tls_outside_brackets = True
                break
        if tls_outside_brackets:
            break
    for word in inside_brackets:
        for i in range(0, len(word) - 3):
            if is_abba(word[i:i + 4]):
                tls_inside_brackets = True
                break
        if tls_inside_brackets:
            break
    if tls_outside_brackets and not tls_inside_brackets:
        count += 1
print(count)