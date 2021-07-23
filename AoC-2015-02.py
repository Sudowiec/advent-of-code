boxes = []
whole_area = 0
whole_ribbon = 0
while True:
    try:
        inp = input()
    except EOFError:
        break
    boxes.append(list(map(int, inp.split("x"))))

for i in boxes:
    sides = []
    areas = []
    areas.append(i[0] * i[1])
    areas.append(i[1] * i[2])
    areas.append(i[2] * i[0])
    sides.append(2 * i[0] + 2 * i[1])
    sides.append(2 * i[1] + 2 * i[2])
    sides.append(2 * i[2] + 2 * i[0])
    volume = i[0] * i[1] * i[2]
    smallest_rib = 99999
    smallest = 99999
    for j in areas:
        if j < smallest:
            smallest = j
    for j in sides:
        if j < smallest_rib:
            smallest_rib = j
    for j in areas:
        whole_area += 2*j
    whole_ribbon += smallest_rib + volume
    whole_area += smallest
print(whole_area, whole_ribbon)