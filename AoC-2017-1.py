inp = list(map(int, input()))
gap = int(len(inp) / 2)
sum_of_digits = 0
for i in range(len(inp)):
    if inp[i] == inp[(i + gap) % len(inp)]:
        sum_of_digits += inp[i]
# if inp[0] == inp[len(inp) - 1]:
    # sum_of_digits += inp[0]
print(sum_of_digits)