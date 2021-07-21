import re
ingredients = {}
ingrset = []
sums = []

while True:
    try:
        inp = input()
    except EOFError:
        break
    mo = re.match(r"(.+): capacity (.+), durability (.+), flavor (.+), texture (.+), calories (.+)", inp)
    ingredients[mo.group(1)] = {"capacity" : int(mo.group(2)), "durability" : int(mo.group(3)), "flavor" : int(mo.group(4)), "texture" : int(mo.group(5)), "calories" : int(mo.group(6))}
    ingrset.append(mo.group(1))
ingreset = set(ingrset)

presums = [0 for i in range(len(ingrset))]
presums.append(100)
maxprd = 0

def summer(step, lvl):
    global ingredients
    global ingrset
    global maxprd
    global presums
    if lvl == len(ingrset) - 1:
        if step > 100:
            return
        print()
        print(presums)
        ingredients_amount = [0, 0, 0, 0, 0]
        for i in range(0, len(presums) - 1):
            div_len = presums[i + 1] - presums[i]
            lf = ingrset[i]
            ingredients_amount[0] += ingredients[lf]["capacity"] * div_len
            ingredients_amount[1] += ingredients[lf]["durability"] * div_len
            ingredients_amount[2] += ingredients[lf]["flavor"] * div_len
            ingredients_amount[3] += ingredients[lf]["texture"] * div_len
            ingredients_amount[4] += ingredients[lf]["calories"] * div_len
        for j in range(len(ingredients_amount) - 1):
            if ingredients_amount[j] <= 0:
                ingredients_amount[j] = 0
        prd = 1
        print(ingredients_amount)
        for i in range(len(ingredients_amount) - 1):
            prd *= ingredients_amount[i]
        print(prd)
        if prd > maxprd and ingredients_amount[4] == 500:
            maxprd = prd
    else:
        for i in range(step + 1, 100):
            presums[lvl + 1] = i
            summer(i, lvl + 1)

summer(0, 0)
print(maxprd)
