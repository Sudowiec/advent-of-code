import re, copy
from collections import defaultdict

FILE_NAME = "2016/11.txt"
FILE_LENGTH = 4

def is_legal(setup):
    for floor in setup:
        if floor == "current_floor" or len(setup[floor]) < 2:
            continue
        pair_check = defaultdict(lambda : [])
        for thingy in setup[floor]:
            pair_check[thingy.split("-")[1]].append(thingy.split("-")[0])
        singles = 0
        for p in pair_check:
            if len(pair_check[p]) < 2:
                singles += 1
        if singles > 1:
            return False
    return True


f = open(FILE_NAME)

setup = {}
for line_number in range(FILE_LENGTH):
    setup[line_number + 1] = []
    inp = f.readline().strip().split(" ")
    if inp[4] == "nothing":
        continue
    for index in range(len(inp)):
        if len(re.findall("generator", inp[index])):
            setup[line_number + 1].append(f"g-{inp[index - 1][0:2]}")
        elif len(re.findall("microchip", inp[index])):
            setup[line_number + 1].append(f"m-{inp[index - 1][0:2]}")
setup["current_floor"] = 1

setups_to_check = [setup]
while True:
    current_setup = setups_to_check.pop(0)
    current_floor = current_setup["current_floor"]
    possible_packages = []
    for thingy in current_setup[current_floor]:
        possible_packages.append([thingy])
    for i in range(len(current_setup[current_floor])):
        for j in range(i + 1, len(current_setup[current_floor])):
            possible_packages.append([current_setup[current_floor][i], current_setup[current_floor][j]])
    for package in possible_packages:
        if current_floor != 4:
            new_setup = copy.deepcopy(current_setup)
            for i in package:
                new_setup[current_floor].remove(i)
            new_setup[current_floor + 1].extend(package)
            new_setup["current_floor"] += 1
            if is_legal(new_setup):
                setups_to_check.append(new_setup)
        if current_floor != 1:
            new_setup = copy.deepcopy(current_setup)
            for i in package:
                new_setup[current_floor].remove(i)
            new_setup[current_floor - 1].extend(package)
            new_setup["current_floor"] -= 1
            if is_legal(new_setup):
                setups_to_check.append(new_setup)
    for i in setups_to_check:
        print(i, is_legal(i))