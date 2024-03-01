FLENGTH = 5
f = open("2016/02.txt")

trans = {10 : "A", 11 : "B", 12 : "C", 13 : "D"}

code = ""
num = 5
for i in range(FLENGTH):
    ins = list(f.readline().strip())
    for j in ins:
        if j == "U":
            if num not in [1, 2, 4, 5, 9]:
                num -= 4 if num in [6, 7, 8, 10, 11, 12] else 2
        elif j == "D":
            if num not in [5, 9, 10, 12, 13]:
                num += 4 if num in [6, 7, 8, 2, 3, 4] else 2
        elif j == "L":
            if num not in [1, 2, 5, 10, 13]:
                num -= 1
        elif j == "R":
            if num not in [1, 4, 9, 12, 13]:
                num += 1
        else:
            raise NameError
    code += str(num) if num < 10 else str(trans[num])
print(code)