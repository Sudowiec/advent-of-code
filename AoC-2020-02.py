import re
sumup = 0
while True:
    try:
        inp = input()
    except EOFError:
        break
    mo = re.match(r"(\d+)-(\d+) (.): (.+)", inp)
    numone = int(mo.group(1))
    numtwo = int(mo.group(2))
    letter = mo.group(3)
    password = mo.group(4)
    lpassword = list(password)
    lto = lpassword[numone - 1]
    ltt = lpassword[numtwo - 1]
    if (lto == letter and not ltt == letter) or (not lto == letter and ltt == letter):
        sumup += 1
print(sumup)