open = ["{", "(", "[", "<"]
closed = ["}",")", "]", ">"]
counter = {"}" : 1197,")" : 3, "]" : 57, ">" : 25137}
tocount = 0
incomp = []
while True:
    try:
        inp = input()
    except EOFError:
        break
    stack = []

    corrupted = False
    for i in inp:
        if i in open:
            stack.append(i)
        if i in closed:
            if open.index(stack[len(stack) - 1]) == closed.index(i):
                stack.pop()
            else:
                tocount += counter[i]
                print(inp, i)
                corrupted = True
                break
    if not corrupted:
        incomp.append("".join(stack))
print(incomp)
inc_counter = {"(" : 1, "[" : 2, "{" : 3, "<" : 4}
scores = []
for s in incomp:
    score = 0
    for i in range(len(s) - 1, -1, -1):
        score *= 5
        score += inc_counter[s[i]]
    scores.append(score)
print(sorted(scores))
print(sorted(scores)[(len(scores) // 2)])

