import re
import copy
aspects = {}
myticket = []
othertickets = []

part = 1
while True:
    try:
        inp = input()
    except EOFError:
        break

    if inp == "":
        part += 1
        continue

    if part == 1:
        mo = re.match(r"(.+): (\d+)-(\d+) or (\d+)-(\d+)", inp)
        aspects[mo.group(1)] = [(int(mo.group(2)), int(mo.group(3))), (int(mo.group(4)), int(mo.group(5)))]

    if part == 2:
        inp = input()
        myticket = list(map(int, inp.split(",")))

    if part == 3:
        if len(othertickets) == 0:
            inp = input()
        othertickets.append(list(map(int, inp.split(","))))

print(aspects)
print(myticket)
print(othertickets)

valid = {}
for i in othertickets:
    for j in i:
        for k in aspects:
            elm = aspects[k]
            if (j >= elm[0][0] and j <= elm[0][1]) or (j >= elm[1][0] and j <= elm[1][1]):
                valid[j] = 1

sumup = 0
ticketspattern = copy.deepcopy(othertickets)
for i in ticketspattern:
    for j in i:
        if j not in valid.keys():
            othertickets.remove(i)
            break
print(othertickets)

order = [0 for i in range(len(aspects))]
# sixty six
validations = {}
for k in aspects:
    valid = True
    tovalid = []
    for i in range(len(othertickets[0])):
        for j in range(len(othertickets)):
            elm = aspects[k]
            if othertickets[j][i] in range(elm[0][0], elm[0][1] + 1) or othertickets[j][i] in range(elm[1][0], elm[1][1] + 1):
                 valid = True
            else:
                valid = False
                break
        if valid:
            tovalid.append(i)
    validations[k] = tovalid

while True:
    for i in validations:
        if len(validations[i]) == 1:
            numtodel = validations[i][0]
            order[numtodel] = i
            for j in validations:
                if numtodel in validations[j]:
                    validations[j].remove(numtodel)
            break
    if not 0 in order:
        break

print(order)



translated = []
for i in range(len(myticket)):
    translated.append((order[i], myticket[i]))
print(translated)

multiplication = 1
for i in translated:
    if i[0][:3] == "dep":
        multiplication *= i[1]
print(multiplication)

