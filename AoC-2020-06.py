from collections import defaultdict

groupanswers = defaultdict(lambda : 0)
members = 0
sumup = 0
while True:
    try:
        inp = list(input())
    except EOFError:
        for i in groupanswers:
            if groupanswers[i] == members:
                sumup += 1
        break

    if inp == []:
        for i in groupanswers:
            if groupanswers[i] == members:
                sumup += 1
        groupanswers = defaultdict(lambda : 0)
        members = 0
    else:
        for i in inp:
            groupanswers[i] += 1
        members += 1

print(sumup)