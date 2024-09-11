import copy

FILE_NAME = "2016/15.txt"
FILE_LENGTH = 6

discs_start = {}
f = open(FILE_NAME)
for line_number in range(FILE_LENGTH):
    inp = f.readline().strip().split(" ")
    discs_start[line_number] = {"positions" : int(inp[3]), "current" : int(inp[11][:-1])}
discs_start[FILE_LENGTH] = {"positions" : 11, "current" : 0}

def rotate_discs(discs, times):
    for disc in discs:
        discs[disc]["current"] = (discs[disc]["current"] + times) % discs[disc]["positions"]

start_time = 0
while True:
    discs = copy.deepcopy(discs_start)
    rotate_discs(discs, start_time)
    goes_through = True
    for position in range(len(discs)):
        rotate_discs(discs, 1)
        if discs[position]["current"] == 0:
            continue
        goes_through = False
        break
    if goes_through:
        print(start_time)
        exit()
    start_time += 1
