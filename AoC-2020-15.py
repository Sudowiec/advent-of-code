from collections import defaultdict
inp = "19,20,14,0,9,1"
inp = inp.split(",")
inp = list(map(int, inp))
print(inp)

apperances = defaultdict(lambda : 0)
spokestack = []

for i in range(30000000):
    if i < len(inp):
        spokestack.append(inp[i])
        apperances[inp[i]] += 1
        if i % 1000 == 0:
            print("saying: " + str(inp[i]))
        continue

    if apperances[spokestack[i - 1]] == 1:
        spokestack.append(0)
        apperances[0] += 1
        if i % 1000 == 0:
            print("saying: 0")
    else:
        for j in range(2, 30000000):
            if spokestack[i - j] == spokestack[i - 1]:
                spokestack.append(j - 1)
                apperances[j - 1] += 1
                if i % 1000 == 0:
                    print("saying: " + str(j - 1))
                break
print(spokestack.pop())

