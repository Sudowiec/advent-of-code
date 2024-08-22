from collections import defaultdict

FILE_NAME = "2016/10.txt"
FILE_LENGTH = 231
LOOKING_FOR = [61, 17]

bots = defaultdict(lambda : {"high" : None, "low" : None, "holding" : []})
outputs = defaultdict(lambda : [])

def print_all():
    print("---")
    for b in bots:
        print(f"bot #{b}: {bots[b]["holding"]}")
    for o in outputs:
        print(f"output #{o}: {outputs[o]}")

f = open(FILE_NAME)
for line_number in range(FILE_LENGTH):
    instruction = f.readline().strip().split(" ")
    if instruction[0] == "value":
        bots[int(instruction[5])]["holding"].append(int(instruction[1]))
    else:
        bots[int(instruction[1])]["low"] = ("b" if instruction[5] == "bot" else "o") + instruction[6]
        bots[int(instruction[1])]["high"] = ("b" if instruction[10] == "bot" else "o") + instruction[11]

while True:
    print_all()
    all_bots_empty = True
    if len(LOOKING_FOR):
        for b in bots:
            if bots[b]["holding"] == LOOKING_FOR or bots[b]["holding"] == LOOKING_FOR[::-1]:
                print(f"FOUND BOT: {b}")
                exit()
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