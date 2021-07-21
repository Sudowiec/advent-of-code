import re
from collections import defaultdict

bags = defaultdict(lambda : [])
while True:
    try:
        inp = input()
    except EOFError:
        break
    mo = re.match(r"(.+) (.+) bags contain (.+)\.", inp)
    bag = mo.group(1) + " " + mo.group(2)
    longinp = mo.group(3)
    bags[bag] = {}
    if mo.group(3) == "no other bags":
        bags[bag] = {}
    else:
        mot = mo.group(3)
        mot = mot.split(",")
        for i in mot:
            elements = i.split(" ")
            if elements[0] == "":
                elements.pop(0)
            elements.pop()
            bags[bag][elements[1] + " " + elements[2]] = int(elements[0])
print(bags)

counter = 0
cache = {}
def golder(bag):
    val = False
    if bag in cache:
        return(cache[bag])
    for i in bags[bag]:
        if i == "shiny gold":
            return True
        else:
            preval = golder(i)
            val = val or preval
            cache[i] = preval
    return val

for bag in bags:
    counter += golder(bag)
print(counter)

def revgolder(bag):
    sumup = 0
    for i in bags[bag]:
        sumup += bags[bag][i] * revgolder(i)
    return 1 + sumup


print(revgolder("shiny gold") - 1)