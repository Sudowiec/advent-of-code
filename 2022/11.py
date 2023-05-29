NUMOFROUNDS = 20
monkeys = []

f = open("2022/11.txt")
cycle = 0
curm = {}
while True:
    l = f.readline()
    if l == "":
        break
    l = l.strip()
    
    if cycle == 0:
        curm["num"] = int(l.split(" ")[1][:-1])
    elif cycle == 1:
        l = l.split(" ")[2:]
        for i in range(len(l)):
            l[i] = l[i].replace(",", "")
        curm["items"] = list(map(int, l))
    elif cycle == 2:
        curm["operation"] = " ".join(l.split(" ")[3:])
    elif cycle == 3:
        curm["test"] = int(l.split(" ")[-1])
    elif cycle == 4:
        curm["true"] = int(l.split(" ")[-1])
    elif cycle == 5:
        curm["false"] = int(l.split(" ")[-1])
    elif cycle == 6:
        monkeys.append(curm)
        curm = {}
        cycle = -1
    cycle += 1

numsOfInspections = [0 for i in range(len(monkeys))]
for r in range(NUMOFROUNDS):
    for monkey in monkeys:
        for i in range(len(monkey["items"])):     
            item = monkey["items"].pop(0)
            numsOfInspections[monkey["num"]] += 1
            op = monkey["operation"].replace("old", str(item))
            item = eval(op) // 3
            if not item % monkey["test"]:
                monkeys[monkey["true"]]["items"].append(item)
            else:
                monkeys[monkey["false"]]["items"].append(item)
numsOfInspections.sort()
print("Monkey buisness:", numsOfInspections[-2] * numsOfInspections[-1])