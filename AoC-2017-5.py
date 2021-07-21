instructions = {}
indx = 0
while True:
    try:
        instructions[indx] = int(input())
    except EOFError:
        break
    indx += 1

pointer = 0
counter = 0
while True:
    try:
        ins = instructions[pointer]
        if ins >= 3:
            instructions[pointer] -= 1
        else:
            instructions[pointer] += 1
        pointer += ins
        counter += 1
        # print(pointer)
    except KeyError:
        print(counter)
        break