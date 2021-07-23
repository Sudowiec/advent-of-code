inp = list(input())
floor = 0
indx = 1
for i in inp:
    if i == '(':
        floor += 1
    else:
        floor -= 1
    if floor < 0: # stage 2
        break
    indx += 1
print(floor, indx)