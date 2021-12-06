fish = list(map(int, input().split(",")))
time = {0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0}
for i in fish:
    time[i] += 1
print(time)

for day in range(256):
    togrow = time[0]
    for i in range(8):
        temp = time[i + 1]
        time[i] = temp
    time[8] = togrow
    time[6] += togrow

sumoffish = 0
for i in time:
    sumoffish += time[i]
print(sumoffish)
