import sys
x=15000
sys.setrecursionlimit(x)
# print(sys.getrecursionlimit())
def match_rules(rules, rule_nums, message):
    # print(message, rule_nums)

    if not rule_nums:
        return not message

    # rule_num, *rule_nums = rule_nums
    rule_num = rule_nums.pop(0)

    rule = rules[rule_num]
    # print(rule)
    if isinstance(rule, str):
        return (message.startswith(rule) and match_rules(rules, rule_nums,message[len(rule):]))
    else:
        b = False
        for option in rule:
            # print(option, rule_nums)
            b = b or match_rules(rules, option + rule_nums, message)
        return b

rules = {}
while True:
    to_append = []
    inp = input()
    if inp == "":
        break

    inp = inp.split(" ")
    index = list(inp[0])
    index.pop()
    index = int("".join(index))
    # print(index)
    inp.pop(0)

    # print(inp)
    shortapp = []
    for i in inp:
        if i == "|":
            to_append.append(shortapp)
            shortapp = []
            continue
        try:
            shortapp.append(int(i))
        except ValueError:
            shortapp.append(i)

    to_append.append(shortapp)

    rules[index] = to_append
    index += 1

for i in rules:
    if rules[i][0] == ["a"]:
        rules[i] = "a"
    elif rules[i][0] == ["b"]:
        rules[i] = "b"

# print(rules)

counter = 0
itr = 0
while True:
    # print(itr)
    try:
        inp = input()
    except EOFError:
        break

    if match_rules(rules, [0], inp):
        counter += 1
    itr += 1

print(counter)
