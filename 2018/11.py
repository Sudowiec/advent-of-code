serial_num = 1723
grid = [["." for j in range(300)] for i in range(300)]

for y in range(len(grid)):
    for x in range(len(grid)):
        rack = x + 11
        power = rack * (y + 1)
        power += serial_num
        power *= rack
        power = list(str(power))
        try:
            power = int(power[len(power) - 3])
        except IndexError:
            power = 0
        power -= 5
        grid[y][x] = power

powers_list = {}
for size in range(1, 301):
    for y in range(len(grid) - size + 1):
        for x in range(len(grid) - size + 1):
            powers = []
            for plusy in range(size):
                for plusx in range(size):
                    powers.append(grid[y + plusy][x + plusx])
            total_power = sum(powers)
            powers_list[str(x + 1) + "," + str(y + 1) + "," + str(size)] = total_power
    print(str(size) + "/300")
lfval = max(powers_list.values())
print(lfval)
for i in powers_list:
    if powers_list[i] == lfval:
        print(i)
