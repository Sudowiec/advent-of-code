input()
inp = input().split(",")

timestamps = {}
t = 0
for i in inp:
    if i == 'x':
        t += 1
    else:
        timestamps[int(i)] = t
        t += 1
print(timestamps)

for i in timestamps:
    print("t mod " + str(i) + " = " + str((i - timestamps[i]) % i) + ";")

minute = 1
while True:
    works = True
    for i in timestamps:
        left = i - (minute % i)
        if minute % i == 0:
            left = 0
        if left != timestamps[i]:
            works = False
            break
    if works:
        print(minute)
        exit(0)
    # print(minute)
    minute += 1