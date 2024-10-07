FILE_NAME = "2016/23.txt"
FILE_LENGTH = 26

instructions = []

f = open(FILE_NAME)
for line_number in range(FILE_LENGTH):
    instruction = f.readline().strip().split(" ")
    for i in range(len(instruction)):
        try:
            instruction[i] = int(instruction[i])
        except:
            pass
    instructions.append(instruction)

toggles = {
    "inc" : "dec",
    "dec" : "inc",
    "jnz" : "cpy",
    "cpy" : "jnz",
    "tgl" : "inc"
}

cpu = {"a" : 7, "b" : 0, "c" : 0, "d" : 0}
index = 0
while index < len(instructions):
    print(instructions)
    print(cpu)
    current_instruction = instructions[index]
    if current_instruction[0] == "cpy":
        if type(current_instruction[1]) is int:
            cpu[current_instruction[2]] = current_instruction[1]
        else:
            cpu[current_instruction[2]] = cpu[current_instruction[1]]
    elif current_instruction[0] == "inc":
        cpu[current_instruction[1]] += 1
    elif current_instruction[0] == "dec":
        cpu[current_instruction[1]] -= 1
    elif current_instruction[0] == "jnz":
        if current_instruction[1] == 1 or cpu[current_instruction[1]] != 0:
            if type(current_instruction[2]) is int:
                index += current_instruction[2] - 1
            else:
                index += cpu[current_instruction[2]] - 1
    elif current_instruction[0] == "tgl":
        if type(current_instruction[1]) is int:
            pos = index + current_instruction[1]
        else:
            pos = index + cpu[current_instruction[1]]
        if pos >= 0 and pos < len(instructions):
            instructions[pos][0] = toggles[instructions[pos][0]]
    index += 1