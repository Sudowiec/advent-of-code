nums = "364289715"
numsl = list(map(int, nums))
length = len(numsl)

node = {"val": numsl.pop(0)}
node["next"] = node
node["prev"] = node
nodehash = {node["val"] : node}
for i in range(999999):
    temp = {"val": 0}
    if i < length - 1:
        temp["val"] = numsl[i]
    else:
        temp["val"] = i + 2
    nodehash[temp["val"]] = temp

    temp["next"] = node
    temp["prev"] = node["prev"]
    node["prev"]["next"] = temp
    node["prev"] = temp

length = 1000000
#
# temp = node
# while True:
#     print(str(temp["val"]) + " ", end='')
#     temp = temp["next"]
#     if temp == node:
#         break
# print()
curr = node
for index in range(10000000):
    # print(index)
    arrone = curr["next"]
    arrtwo = curr["next"]["next"]
    arrthree = curr["next"]["next"]["next"]
    sub = 1
    while True:
        destval = ((curr["val"] - sub - 1) % length) + 1
        if arrone["val"] == destval:
            sub += 1
            continue
        if arrtwo["val"] == destval:
            sub += 1
            continue
        if arrthree["val"] == destval:
            sub += 1
            continue
        break
    destination = nodehash[destval]
    # while True:
    #     destination = destination["next"]
    #     if destval == destination["val"]:
    #         break

    curr["next"] = arrthree["next"]
    arrthree["next"]["prev"] = curr
    arrone["prev"] = destination
    arrthree["next"] = destination["next"]
    destination["next"] = arrone

    curr = curr["next"]

    # temp = node
    # while True:
    #     print(temp["val"], end='')
    #     temp = temp["next"]
    #     if temp == node:
    #         break
    # print()
print(nodehash[1]["next"]["val"] * nodehash[1]["next"]["next"]["val"])

