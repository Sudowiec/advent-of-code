import os, sys, time, random
from collections import defaultdict

FILE_NAME = "2016/10.txt"
FILE_LENGTH = 231
LOOKING_FOR = [61, 17]

BOT_EYES = ["O", "U", "I", "0", "P", "D", "A", "^", "|", "+", "@", "*", "-", "=", "<", ">", "~", "'"]
BOT_MOUTHS = ["w", "m", "_", ".", ","]
MAX_BOT_WIDTH = 12
MAX_BOT_HEIGHT = 6
MAX_OUTPUT_WIDTH = 5
DELAY = 0.3

COL_RESET = "\033[0;0m"
COL_RED = "\033[1;31m"
COL_GREEN = "\033[0;32m"
COL_BLUE = "\033[94m"

bots = defaultdict(lambda : {"face" : get_bot_face(), "high" : None, "low" : None, "holding" : []})
outputs = {}

def get_bot_face():
    eye = random.choice(BOT_EYES)
    mouth = random.choice(BOT_MOUTHS)
    return f"{eye}{mouth}{eye}"

def build_bot(bot_id):
    holding = list(map(str, bots[bot_id]["holding"]))
    face = bots[bot_id]["face"]
    h0 = holding[0] if len(holding) > 0 else ""
    h1 = holding[1] if len(holding) > 1 else ""
    if bot_id == correct_bot:
        antenna = f"{' ' * 5}{COL_GREEN}|{COL_RESET}{' ' * 5}"
    else:
        antenna = f"{' ' * 5}{COL_RED}|{COL_RESET}{' ' * 5}"
    head = f"{' ' * 3}[{face}]{' ' * 3}"
    belly = f"{' ' * (2 - len(h0))}[{COL_BLUE}{h0}{COL_RESET}][#][{COL_BLUE}{h1}{COL_RESET}]{' ' * (2 - len(h1))}"
    legs = f"{' ' * 4}] [{' ' * 4}"
    return [antenna, head, belly, legs]    

def print_bots(bot_list, rows, cols, come_back = True):
    to_print = ""
    for r in range(rows):
        to_print += "\n"
        current_bots = bot_list[r * cols : (r + 1) * cols]
        for layer in range(4):
            for c in current_bots:
                to_print += c[layer] + " "
            to_print += "\n"
        to_print += "\n"
    sys.stdout.write(to_print)
    print_outputs()
    if come_back:
        sys.stdout.write("\033[F" * (to_print.count("\n") + 3))

def print_outputs():
    to_print = "\n" + "   +---+    " * len(outputs) + "\n"
    for output in outputs:
        value = str(outputs[output])
        if len(value) == 0:
            value = "   "
        elif len(value) == 1:
            value = f" {value} "
        else:
            value = f"{value} "
        to_print += f"   |{COL_BLUE}{value}{COL_RESET}|    "
    to_print += "\n" + "   +---+    " * len(outputs)
    sys.stdout.write(to_print)

f = open(FILE_NAME)
for line_number in range(FILE_LENGTH):
    instruction = f.readline().strip().split(" ")
    if instruction[0] == "value":
        bots[int(instruction[5])]["holding"].append(int(instruction[1]))
    else:
        bots[int(instruction[1])]["low"] = ("b" if instruction[5] == "bot" else "o") + instruction[6]
        bots[int(instruction[1])]["high"] = ("b" if instruction[10] == "bot" else "o") + instruction[11]
        if instruction[5] == "output":
            outputs[int(instruction[6])] = ""
        if instruction[10] == "output":
            outputs[int(instruction[11])] = ""

terminal_size = os.get_terminal_size()
num_of_bots_in_row = int(terminal_size.columns / MAX_BOT_WIDTH) - 1
num_of_bots_in_column = int(len(bots) / num_of_bots_in_row) + 1

print(num_of_bots_in_row, num_of_bots_in_column, len(outputs))
if num_of_bots_in_row < len(outputs) or terminal_size.columns < num_of_bots_in_row * MAX_BOT_WIDTH or terminal_size.lines < num_of_bots_in_column * MAX_BOT_HEIGHT + 3:
    print("Terminal too small!")
    exit(1)

correct_bot = None
os.system("cls")
while True:
    time.sleep(DELAY)
    bots_to_print = []
    for b in bots:
        bots_to_print.append(build_bot(b))
    print_bots(bots_to_print, num_of_bots_in_column, num_of_bots_in_row)
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
                outputs[int(high_target[1:])] = high_value

            low_value = min(bots[b]["holding"])
            low_target = bots[b]["low"]
            if low_target[0] == "b":
                bots[int(low_target[1:])]["holding"].append(low_value)
            else:
                outputs[int(low_target[1:])] = low_value

            bots[b]["holding"] = []
            # break
    if all_bots_empty:
        break
print_bots(bots_to_print, num_of_bots_in_column, num_of_bots_in_row, False)