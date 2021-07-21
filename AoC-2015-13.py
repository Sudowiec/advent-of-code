import re
from collections import defaultdict
people_set = []
whole_list = defaultdict(lambda: [])
all_perms = []
current_perm = []
total_happiness = 0

def perms(xset, depth):
    global current_perm
    global all_perms
    for i in xset:
        current_perm.append(i)
        if len(xset) == 1:
            all_perms.append(current_perm.copy())
            print(current_perm)
            current_perm.pop()
            return()
        xset_copy = xset.copy()
        xset_copy.remove(i)
        perms(xset_copy, depth + 1)
        current_perm.pop()


while True:
    try:
        inp = input()
    except EOFError:
        break
    # Alice would gain 54 happiness units by sitting next to Bob.
    match = re.match(r"(.+) would (.+) (\d+) happiness units by sitting next to (.+)\.", inp)
    person = match.group(1)
    people_set.append(person)
    rel_person = match.group(4)
    amount = int(match.group(3))
    if match.group(2) == "lose":
        amount -= 2 * amount
    whole_list[person].append({rel_person : amount})
people_set = set(people_set)

for i in people_set:
    whole_list["Santa"].append({i : 0})
    whole_list[i].append({"Santa" : 0})
people_set.add("Santa")

# print(whole_list)
# print(people_set)

perms(people_set, 0)
# print(all_perms)

for i in all_perms:
    happiness = 0
    for j in range(len(i)):
        pair = [i[j], i[(j + 1) % len(i)]]
        for k in whole_list[pair[0]]:
            if pair[1] in k:
                happiness += k[pair[1]]
        for k in whole_list[pair[1]]:
            if pair[0] in k:
                happiness += k[pair[0]]
    if happiness > total_happiness:
        total_happiness = happiness
print(total_happiness)