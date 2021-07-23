from collections import defaultdict
wireone = input().split(",")
wiretwo = input().split(",")
locations = defaultdict(lambda: 0)
locations_steps = {}

x = 0
y = 0
step = 0
for i in wireone:
    if i[:1] == 'U':
        for j in range(int(i[1:])):
            step += 1
            y += 1
            locations[",".join([str(x), str(y)])] += 1
            locations_steps[",".join([str(x), str(y)])] = step

    elif i[:1] == 'D':
        for j in range(int(i[1:])):
            step += 1
            y -= 1
            locations[",".join([str(x), str(y)])] += 1
            locations_steps[",".join([str(x), str(y)])] = step

    elif i[:1] == 'R':
        for j in range(int(i[1:])):
            step += 1
            x += 1
            locations[",".join([str(x), str(y)])] += 1
            locations_steps[",".join([str(x), str(y)])] = step

    elif i[:1] == 'L':
        for j in range(int(i[1:])):
            step += 1
            x -= 1
            locations[",".join([str(x), str(y)])] += 1
            locations_steps[",".join([str(x), str(y)])] = step


x = 0
y = 0
shortest = 9999999
step = 0
for i in wiretwo:
    if i[:1] == 'U':
        for j in range(int(i[1:])):
            step += 1
            y += 1
            if locations[",".join([str(x), str(y)])] > 0:
                dist = locations_steps[",".join([str(x), str(y)])] + step
                if dist < shortest:
                    shortest = dist
                    print(x, y)

    elif i[:1] == 'D':

        for j in range(int(i[1:])):
            step += 1
            y -= 1
            if locations[",".join([str(x), str(y)])] > 0:
                dist = locations_steps[",".join([str(x), str(y)])] + step
                if dist < shortest:
                    shortest = dist
                    print(x, y)

    elif i[:1] == 'R':

        for j in range(int(i[1:])):
            step += 1
            x += 1
            if locations[",".join([str(x), str(y)])] > 0:
                dist = locations_steps[",".join([str(x), str(y)])] + step
                if dist < shortest:
                    shortest = dist
                    print(x, y)

    elif i[:1] == 'L':
        for j in range(int(i[1:])):
            step += 1
            x -= 1
            if locations[",".join([str(x), str(y)])] > 0:
                dist = locations_steps[",".join([str(x), str(y)])] + step
                if dist < shortest:
                    shortest = dist
                    print(x, y)


print(locations)
print(locations_steps)

# shortest = 9999999
# for i in locations:
#     if locations[i] > 1:
#         arr = i.split(",")
#         dist = abs(int(arr[0])) + abs(int(arr[1]))
#         if dist < shortest:
#             shortest = dist
#             print(i)
print(shortest)