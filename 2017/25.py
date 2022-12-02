from collections import defaultdict

steps = 12425180
# steps = 6

state = "A"
tape = defaultdict(lambda : 0)
pos = 0

def step():
    global pos, state
    if tape[pos] == 0:
        match state:
            case "A":
                tape[pos] = 1
                pos += 1
                state = "B"
            case "B":
                tape[pos] = 0
                pos -= 1
                state = "B"
            case "C":
                tape[pos] = 1
                pos -= 1
                state = "D"
            case "D":
                tape[pos] = 1
                pos -= 1
                state = "E"
            case "E":
                tape[pos] = 1
                pos -= 1
                state = "F"
            case "F":
                tape[pos] = 1
                pos += 1
                state = "A"
        # match state:
        #     case "A":
        #         tape[pos] = 1
        #         pos += 1
        #         state = "B"
        #     case "B":
        #         tape[pos] = 1
        #         pos -= 1
        #         state = "A"
    elif tape[pos] == 1:
        match state:
            case "A":
                tape[pos] = 0
                pos += 1
                state = "F"
            case "B":
                tape[pos] = 1
                pos -= 1
                state = "C"
            case "C":
                tape[pos] = 0
                pos += 1
                state = "C"
            case "D":
                tape[pos] = 1
                pos += 1
                state = "A"
            case "E":
                tape[pos] = 0
                pos -= 1
                state = "D"
            case "F":
                tape[pos] = 0
                pos -= 1
                state = "E"
        # match state:
        #     case "A":
        #         tape[pos] = 0
        #         pos -= 1
        #         state = "B"
        #     case "B":
        #         tape[pos] = 1
        #         pos += 1
        #         state = "A"

for i in range(steps):
    step()
print(sum(list(tape.values())))
