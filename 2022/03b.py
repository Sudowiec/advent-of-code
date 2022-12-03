sumVal = 0
while True:
    try:
        inpOne = list(input())
        inpTwo = list(input())
        inpThree = list(input())
    except EOFError:
        break
    searchOne = set(inpOne).intersection(inpTwo)
    searchTwo = list(set(searchOne).intersection(inpThree))[0]
    sumVal += ord(searchTwo) - 96 if ord(searchTwo) >= 97 else ord(searchTwo) - 38
print(sumVal)