elves = []
curcal = 0
while True:
    try:
        inp = input()
    except EOFError:
        break

    if (inp == ''):
        elves.append(curcal)
        curcal = 0
        continue

    curcal += int(inp)
print(sum(sorted(elves)[-3:]))