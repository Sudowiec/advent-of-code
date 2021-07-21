program = list(map(int, input().split(",")))

for i in range(1, 100):
    for j in range(1, 100):
        instructions = program.copy()
        noun = i
        verb = j
        instructions[1] = noun
        instructions[2] = verb
        for k in range(0, len(instructions), 4):
            if instructions[k] == 1:
                instructions[instructions[k + 3]] = instructions[instructions[k + 1]] + instructions[instructions[k + 2]]
            elif instructions[k] == 2:
                instructions[instructions[k + 3]] = instructions[instructions[k + 1]] * instructions[instructions[k + 2]]
            elif instructions[k] == 99:
                if instructions[0] == 19690720:
                    print(100 * noun + verb)