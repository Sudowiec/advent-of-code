from collections import defaultdict
inp = 34000000
houses = defaultdict(lambda : 0)

house = 1
while True:
    presents = 0
    for i in range(1, house + 1):
        if house % i == 0:
            presents += i * 10
    print(house, presents)
    if presents >= inp:
        print(house)
        break
    house += 1

# for elf in range(1, inp + 1):
#     index = 0
#     for i in range(elf, inp, elf):
#         houses[i] += elf*11
#         index += 1
#         if index == 50:
#             break
#     # print(elf)
#
# for i in houses:
#     if houses[i] >= 34000000:
#         print("end: ", i)
#         break
