import re
import copy
plant_hash = {}
for i in range(50):
    plant_hash[i - 50] = "."
margin = -48
pattern_hash = {}

plantation = input()
mo = re.match(r"initial state: (.+)", plantation)
plantation = mo.group(1)
plantation = list(plantation)
for i in range(len(plantation) + 150):
    try:
        plant_hash[i] = plantation[i]
    except IndexError:
        plant_hash[i] = "."
input()

while True:
    try:
        inp = input()
    except EOFError:
        break

    mo = re.match(r"(.{5}) => (.)", inp)
    pattern_hash[mo.group(1)] = mo.group(2)
print(plant_hash)
print(pattern_hash)


print("".join(plant_hash.values()))
for time in range(110):
    changable_plant_hash = copy.deepcopy(plant_hash)
    for i in range(margin, len(plant_hash) - 52):
        lflist = []
        for j in range(i - 2, i + 3):
            lflist.append(plant_hash[j])
        lflist = "".join(lflist)

        matched = False
        for j in pattern_hash:
            if j == lflist:
                changable_plant_hash[i] = pattern_hash[j]
                matched = True
                break
        if not matched:
            changable_plant_hash[i] = "."

    print("".join(changable_plant_hash.values()))
    plant_hash = copy.deepcopy(changable_plant_hash)
    counter = 0
    for i in plant_hash:
        if plant_hash[i] == "#":
            counter += i
    print(counter, time)


print(plant_hash)
counter = 0
for i in plant_hash:
    if plant_hash[i] == "#":
        counter += i
print(counter)