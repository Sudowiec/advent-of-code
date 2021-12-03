from collections import defaultdict
BYTELEN = 12

ones = defaultdict(lambda : 0)
zeroes = defaultdict(lambda : 0)
while True:
    try:
        inp = list(input())
    except EOFError:
        break

    for i in range(BYTELEN):
        if inp[len(inp) - i - 1] == "0":
            zeroes[len(inp) - i - 1] += 1
        elif inp[len(inp) - i - 1] == "1":
            ones[len(inp) - i - 1] += 1

gamma = ["x" for i in range(BYTELEN)]
epsylon = ["x" for i in range(BYTELEN)]
for i in range(BYTELEN):
    if ones[i] > zeroes[i]:
        gamma[i] = 1
        epsylon[i] = 0
    elif ones[i] < zeroes[i]:
        gamma[i] = 0
        epsylon[i] = 1
gammadec = int("".join(list(map(str, (gamma)))), 2)
epsylondec = int("".join(list(map(str, (epsylon)))), 2)
epsylondec = int("".join(list(map(str, (epsylon)))), 2)

print(gammadec * epsylondec)