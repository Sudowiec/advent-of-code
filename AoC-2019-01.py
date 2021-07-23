import math
sumup = 0
while True:
    try:
        intiger = math.floor(int(input()) / 3) - 2
        sumup += intiger
        fuel = intiger
        while True:
            fuel = math.floor(fuel / 3) - 2
            if fuel <= 0:
                break
            sumup += fuel
    except EOFError:
        print(sumup)
        break