one = int(input())
two = int(input())
three = int(input())
counter = 0
while True:
    prevres = one + two + three
    one = two
    two = three
    try:
        three = int(input())
    except EOFError:
        break
    res = one + two + three
    if res > prevres:
        counter += 1
print(counter)