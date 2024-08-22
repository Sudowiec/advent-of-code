FILE_NAME = "2016/09.txt"
f = open(FILE_NAME)

def decompress(string, multiplication):
    uncompressed_length = 0
    sign_index = 0
    while sign_index < len(string):
        if string[sign_index] != "(":
            uncompressed_length += 1
            sign_index += 1
            continue
        else:
            for i in range(sign_index, len(string)):
                if string[i] == ")":
                    ending_bracket_index = i
                    break
            instructions = list(map(int, string[sign_index + 1: ending_bracket_index].split("x")))
            uncompressed_length += decompress(string[ending_bracket_index + 1:ending_bracket_index + 1 + instructions[0]], instructions[1])
            sign_index = ending_bracket_index + 1 + instructions[0]
    return uncompressed_length * multiplication

input = f.readline().strip()
uncompressed_length = decompress(input, 1)
print(uncompressed_length)