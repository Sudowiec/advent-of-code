FILE_NAME = "2016/12.txt"
FILE_LENGTH = 23

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

# cpu = {"a" : 0, "b" : 0, "c" : 0, "d" : 0}
cpu = {"a" : 0, "b" : 0, "c" : 1, "d" : 0}
index = 0
while index < len(instructions):
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
            index += current_instruction[2] - 1
    index += 1
print(cpu)