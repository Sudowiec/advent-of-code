FLENGTH = 5
f = open("2016/02.txt")

code = ""
num = 5
for i in range(FLENGTH):
    ins = list(f.readline().strip())
    for j in ins:
        if j == "U":
            if num > 3:
                num -= 3
        elif j == "D":
            if num < 7:
                num += 3
        elif j == "L":
            if num not in [1, 4, 7]:
                num -= 1
        elif j == "R":
            if num not in [3, 6, 9]:
                num += 1
        else:
            raise NameError
    code += str(num)
print(code)