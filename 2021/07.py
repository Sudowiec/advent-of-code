crabs = list(map(int, input().split(",")))
highest = max(crabs)

less = 99999999
for goal in range(0, highest + 1):
    fuel = 0
    for i in crabs:
        steps = abs(i - goal)
        fuel += int(((2 + (steps - 1)) / 2) * steps)
    if fuel < less:
        less = fuel
print(less)