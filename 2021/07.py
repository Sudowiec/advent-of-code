crabs = list(map(int, input().split(",")))
highest = max(crabs)

less = 999999
for goal in range(0, highest + 1):
    fuel = 0
    for i in crabs:
        fuel += abs(i - goal)
    if fuel < less:
        less = fuel
print(less)