import os, sys, time, random
from collections import defaultdict

FILE_NAME = "2016/10.txt"
FILE_LENGTH = 231
LOOKING_FOR = []

BOT_EYES = ["O", "U", "I", "0", "P", "D", "A", "^", "|", "+", "@", "*", "-", "=", "<", ">", "~", "'"]
BOT_MOUTHS = ["w", "m", "_", ".", ","]
MAX_BOT_WIDTH = 12
MAX_OUTPUT_WIDTH = 5

bots = defaultdict(lambda : {"high" : None, "low" : None, "holding" : []})
outputs = defaultdict(lambda : [])

def get_bot_face():
    eye = random.choice(BOT_EYES)
    mouth = random.choice(BOT_MOUTHS)
    return f"{eye}{mouth}{eye}"

def print_bot(bot_id, is_correct = False):
    holding = list(map(str, bots[bot_id]["holding"]))
    h0 = holding[0] if len(holding) > 0 else ""
    h1 = holding[1] if len(holding) > 1 else ""
    antenna = f"{" " * (len(h0) + 3)}|"
    head = f"{" " * (len(h0) + 1)}[{get_bot_face()}]"
    belly = f"[{h0}][ ][{h1}]"
    legs = f"{" " * (len(h0) + 2)}] ["
    to_print = f"{antenna}\n{head}\n{belly}\n{legs}\n\n"
    sys.stdout.write(to_print)

def print_output(output_id):
    holding = outputs[output_id]
    box_size = len(str(max(holding)))
    holding = list(map(str, holding))
    to_print = ""
    to_print += f"{("_" * (box_size + 2))}\n"
    for value in holding:
        to_print += f"|{value}{" " * (box_size - len(value))}|\n"
    sys.stdout.write(to_print + "\n")

    
f = open(FILE_NAME)
for line_number in range(FILE_LENGTH):
    instruction = f.readline().strip().split(" ")
    if instruction[0] == "value":
        bots[int(instruction[5])]["holding"].append(int(instruction[1]))
    else:
        bots[int(instruction[1])]["low"] = ("b" if instruction[5] == "bot" else "o") + instruction[6]
        bots[int(instruction[1])]["high"] = ("b" if instruction[10] == "bot" else "o") + instruction[11]

correct_bot = None
while True:
    all_bots_empty = True
    if len(LOOKING_FOR) and not correct_bot:
        for b in bots:
            if bots[b]["holding"] == LOOKING_FOR or bots[b]["holding"] == LOOKING_FOR[::-1]:
                correct_bot = b
                break
    for b in bots:
        if len(bots[b]["holding"]) == 2:
            all_bots_empty = False

            high_value = max(bots[b]["holding"])
            high_target = bots[b]["high"]
            if high_target[0] == "b":
                bots[int(high_target[1:])]["holding"].append(high_value)
            else:
                outputs[int(high_target[1:])].append(high_value)

            low_value = min(bots[b]["holding"])
            low_target = bots[b]["low"]
            if low_target[0] == "b":
                bots[int(low_target[1:])]["holding"].append(low_value)
            else:
                outputs[int(low_target[1:])].append(low_value)

            bots[b]["holding"] = []
            break
    if all_bots_empty:
        break

for i in outputs:
    print_output(i)
print(len(bots))
s = os.get_terminal_size()
print(s.columns, s.lines)