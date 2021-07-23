import re

def count(listed):
    countable = listed.split(" ")
    while "+" in countable:
        index = -1
        for i in range(len(countable)):
            if countable[i + 1] == "+":
                ctsr = "".join(countable[i : i + 3])
                num = eval(ctsr)
                index = i
                break
        for j in range(3):
            countable.pop(index)
        countable.insert(index, str(num))
    amount = eval("".join(countable))

    return int(amount)

whole_count = 0
while True:
    try:
        inp = input()
    except EOFError:
        break
    # print(inp)
    while "(" in inp and ")" in inp:
        beginning = -1
        end = -1
        counted = -1
        to_count = ""

        for i in range(len(inp)):

            if inp[i] == "(":
                beginning = i
            elif inp[i] == ")":
                end = i

            if beginning != -1 and end != -1:
                to_count = inp[beginning + 1 : end]
                # print(to_count)
                counted = count(to_count)
                # print(counted)
                break

        to_count = re.sub("\*", "\\\*", to_count)
        to_count = re.sub("\+", "\\\+", to_count)
        inp = re.sub("\(" + to_count + "\)", str(counted), inp)
        # print(inp)
    whole_count += count(inp)
print(whole_count)
