import hashlib
input = "yzbqklnj"
number = 1
while True:
    m = hashlib.md5()
    testput = input + str(number)
    m.update(testput.encode("ASCII"))
    m = m.hexdigest()
    if str(m)[:6] == "000000":
        print(number, m[:6])
        exit(0)
    # print(number, m[:6])
    number += 1