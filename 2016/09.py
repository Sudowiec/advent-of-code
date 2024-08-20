FILE_NAME = "2016/09.txt"
f = open(FILE_NAME)

input = f.readline().strip()
uncompressed_length = 0
sign_index = 0
while sign_index < len(input):
    if input[sign_index] != "(":
        uncompressed_length += 1
        sign_index += 1
        continue
    else:
        for i in range(sign_index, len(input)):
            if input[i] == ")":
                ending_bracket_index = i
                break
        instructions = list(map(int, input[sign_index + 1: ending_bracket_index].split("x")))
        sign_index += instructions[0] + ending_bracket_index - sign_index + 1
        uncompressed_length += instructions[0] * instructions[1]
print(uncompressed_length)