import re
from collections import defaultdict

cities = []
all_perms = []
current_perm = []
cities_vals = defaultdict(lambda: [])
def perms(xset, depth):
    global current_perm
    global all_perms
    for i in xset:
        current_perm.append(i)
        if len(xset) == 1:
            all_perms.append(current_perm.copy())
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
    mo = re.match(r"(.+) to (.+) = (\d+)", inp)
    city1 = mo.group(1)
    city2 = mo.group(2)
    val = mo.group(3)
    cities.append(city1)
    cities.append(city2)
    cities_vals[city1].append({city2 : val})
cities = set(cities)
perms(cities, 0)
print(cities)
print(cities_vals)
# print(all_perms)

distances = []
for i in all_perms:
    distance = 0
    for j in range(1, len(i)):

        cityone = i[j - 1]
        citytwo = i[j]
        values = cities_vals[cityone]
        picked = False
        for k in values:
            if citytwo in k:
                distance += int(k[citytwo])
                picked = True
                break
        if not picked:
            values = cities_vals[citytwo]
            for k in values:
                if cityone in k:
                    distance += int(k[cityone])
    distances.append(distance)

print(max(distances))