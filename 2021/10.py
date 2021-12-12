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

    for i in inp:
        if i in open:
            stack.append(i)
        if i in closed:
            if open.index(stack[len(stack) - 1]) == closed.index(i):
                stack.pop()
            else:
                tocount += counter[i]
                print(inp, i)
                break
    incomp.append(inp)
print(tocount)