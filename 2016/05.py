import hashlib
import sys
import random
inp = "abbhdwsy"

TO_ANIMATE = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()<>?|\\"
COL_RESET = "\033[0;0m"
COL_RED = "\033[1;31m"
COL_GREEN = "\033[0;32m"

ind = 0
pw = list("________")
count = 0
while True:
    count += 1
    m = hashlib.md5()
    m.update((inp + str(ind)).encode('utf-8'))
    hex_m = m.hexdigest()
    if hex_m[0:5] == '00000':
        if hex_m[5] in "01234567" and pw[int(hex_m[5])] == "_":
            pw[int(hex_m[5])] = str(hex_m[6])
    printpw = []
    if count % 1000 == 0:
        for i in range(len(pw)):
            if pw[i] == "_":
                printpw.extend([COL_RED, TO_ANIMATE[random.randint(0, len(TO_ANIMATE) - 1)]])
            else:
                printpw.extend([COL_GREEN, pw[i]])
        sys.stdout.write("".join(printpw) + COL_RESET + "\r")
    ind += 1
    if "_" not in pw:
        break
sys.stdout.write(COL_GREEN + "".join(pw) + COL_RESET + "\n")