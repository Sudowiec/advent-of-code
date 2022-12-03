sumVal = 0
while True:
    try:
        inp = list(input())
    except EOFError:
        break
    l = len(inp)
    firstHalf = inp[:int(l / 2)]
    secondHalf = inp[int(l / 2):]
    lfElem = list(set(firstHalf).intersection(secondHalf))[0]
    sumVal += ord(lfElem) - 96 if ord(lfElem) >= 97 else ord(lfElem) - 38
print(sumVal)