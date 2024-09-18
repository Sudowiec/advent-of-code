FILE_NAME = "2016/22.txt"
FILE_LENGTH = 992

filesystem = {}
f = open(FILE_NAME)
for line_number in range(FILE_LENGTH):
    input = f.readline()
    if line_number < 2:
        continue
    input = list(filter(('').__ne__, input.strip().split(" ")))
    coords = input[0].split("/")[3].split("-")
    x = int(coords[1][1:])
    y = int(coords[2][1:])
    size = int(input[1][:-1])
    used = int(input[2][:-1])
    filesystem[f"{x},{y}"] = {"size" : size, "used" : used}

count = 0
for node_a in filesystem:
    for node_b in filesystem:
        if node_a == node_b:
            continue
        if filesystem[node_a]["used"] == 0:
            continue
        if filesystem[node_b]["size"] - filesystem[node_b]["used"] < filesystem[node_a]["used"]:
            continue
        count += 1
print(count)