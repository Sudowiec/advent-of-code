import hashlib
inp = "abbhdwsy"
ind = 0
pw = ""
while True:
    m = hashlib.md5()
    m.update((inp + str(ind)).encode('utf-8'))
    hex_m = m.hexdigest()
    if hex_m[0:5] == '00000':
        pw += str(hex_m[5])
        print(pw)
    ind += 1
    if len(pw) > 7:
        break