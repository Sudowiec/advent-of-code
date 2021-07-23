import copy
deck = []
while True:
    try:
        inp = input()
    except EOFError:
        preptdeck = deck
        break
    if inp == "":
        prepodeck = deck
        deck = []
        continue
    if inp[0] != "P":
        deck.append(int(inp))
podeck = copy.deepcopy(prepodeck)
ptdeck = copy.deepcopy(preptdeck)
print(podeck)
print(ptdeck)

while len(podeck) > 0 and len(ptdeck) > 0:
    cardo = podeck.pop(0)
    cardt = ptdeck.pop(0)
    if cardo > cardt:
        podeck.append(cardo)
        podeck.append(cardt)
    elif cardo < cardt:
        ptdeck.append(cardt)
        ptdeck.append(cardo)
    else:
        exit(2)
if len(podeck) == 0:
    winner = ptdeck
elif len(ptdeck) == 0:
    winner = podeck

score = 0
for i in range(len(winner)):
    score += winner[len(winner) - i - 1] * (i + 1)
print(score)

podeck = copy.deepcopy(prepodeck)
ptdeck = copy.deepcopy(preptdeck)

def rec(deckone, decktwo):
    check = {}
    wholewinner = 0
    while len(deckone) > 0 and len(decktwo) > 0:
        if ",".join(list(map(str, deckone))) + "." + ",".join(list(map(str, decktwo))) in check:
            wholewinner = 1
            break
        check[",".join(list(map(str, deckone))) + "." + ",".join(list(map(str, decktwo)))] = 1
        cardo = deckone.pop(0)
        cardt = decktwo.pop(0)

        if cardo < len(deckone) + 1 and cardt < len(decktwo) + 1:
            winner = rec(deckone[:cardo], decktwo[:cardt])
        else:
            if cardo > cardt:
                winner = 1
            else:
                winner = 2
        if winner == 1:
            deckone.append(cardo)
            deckone.append(cardt)
        elif winner == 2:
            decktwo.append(cardt)
            decktwo.append(cardo)

    if len(decktwo) == 0 and wholewinner == 0:
        windeck = deckone
        wholewinner = 1
    elif len(deckone) == 0 and wholewinner == 0:
        windeck = decktwo
        wholewinner = 2
    elif wholewinner == 1:
        windeck = deckone

    score = 0
    for i in range(len(windeck)):
        score += windeck[len(windeck) - i - 1] * (i + 1)
    print(score)
    return wholewinner

rec(podeck, ptdeck)

