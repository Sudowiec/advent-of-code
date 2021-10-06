inp = "919901"
checkinp = list(map(int, list(str(inp))))
recipe = [3, 7]
indone = 0
indtwo = 1
# print(recipe, indone, indtwo)

indx = 0
while True:
    valone = recipe[indone]
    valtwo = recipe[indtwo]
    mainval = valone + valtwo

    if mainval >= 10:
        mainval = list(str(mainval))
        recipe.append(int(mainval[0]))
        recipe.append(int(mainval[1]))
    else:
        recipe.append(mainval)

    indone += (1 + valone)
    indone %= len(recipe)
    indtwo += (1 + valtwo)
    indtwo %= len(recipe)

    if len(recipe) > len(checkinp):
        cut = recipe[len(recipe) - len(checkinp):len(recipe)]
        # print(cut)
        if cut == checkinp:
            # print(recipe, indone, indtwo)
            print(len(recipe) - len(checkinp))
            exit(0)
    indx += 1
    # print(recipe, indone, indtwo)

