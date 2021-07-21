import hashlib
import re
hash_func = hashlib.md5()
input = "ioramepc"
road_que = [["", 0, 0]]
dirlist = ["U", "D", "L", "R"]
xhash = {"U" : 0, "D" : 0, "L": -1, "R" : 1}
yhash = {"U" : -1, "D" : 1, "L": 0, "R" : 0}
step = 0

while True:
    three = road_que.pop(0)
    element = three[0]
    x = three[1]
    y = three[2]
    # print(three)
    if x < 0 or x > 3 or y < 0 or y > 3:
        continue
    if x == 3 and y == 3:
        print(step, len(element), element)
        step += 1
        continue
    # element_check = element
    # element_check = re.sub(r"R(.*)L", r"\1", element_check)
    # element_check = re.sub(r"U(.*)D", r"\1", element_check)
    # element_check = re.sub(r"L(.*)R", r"\1", element_check)
    # element_check = re.sub(r"D(.*)U", r"\1", element_check)
    # if re.search(r"(R.*){3}", element_check) and not re.search(r"(R.*){4}", element_check):
    #     if re.search(r"(D.*){3}", element_check) and not re.search(r"(D.*){4}", element_check):
    #         if len(element_check) == 6:
    #             print(element, element_check)
    #             exit(0)
    # print(element)
    cipher = input + element
    hash_func = hashlib.md5()
    hash_func.update(cipher.encode("ASCII"))
    cipher = hash_func.hexdigest()

    for i in range(4):
        if re.search(r"([bcdef])", cipher[i]):
            resx = x + xhash[dirlist[i]]
            resy = y + yhash[dirlist[i]]
            road_que.append([element + dirlist[i], resx, resy])
    step += 1
# DRURDRUDDLLDLUURRDULRLDUUDDDRR
# DRURDRUDDLLDLUURRDULRLDUUDDDRR


