import hashlib
inp = "abbhdwsy"
ind = 0
pw = list("________")
while True:
    m = hashlib.md5()
    m.update((inp + str(ind)).encode('utf-8'))
    hex_m = m.hexdigest()
    if hex_m[0:5] == '00000':
        if hex_m[5] in "01234567" and pw[int(hex_m[5])] == "_":
            pw[int(hex_m[5])] = str(hex_m[6])
            print("".join(pw))
    ind += 1
    if "_" not in pw:
        break