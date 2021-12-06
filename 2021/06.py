fish = list(map(int, input().split(",")))
fishhash = {}
highest = len(fish) - 1
for i in range(len(fish)):
    fishhash[i] = fish[i]

for index in range(256):
    tospawn = 0
    for i in fishhash:
        if fishhash[i] == 0:
            fishhash[i] = 7
            tospawn += 1
        fishhash[i] -= 1

    for i in range(tospawn):
        highest += 1
        fishhash[highest] = 8

print(highest)
