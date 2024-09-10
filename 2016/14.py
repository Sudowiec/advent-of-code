import hashlib, os, sys

KEY_STRETCH = 2016
SALT = "abc"

def hash_string(s, stretch_val):
    md5 = hashlib.md5(s.encode()).hexdigest()
    while stretch_val > 0:
        md5 = hashlib.md5(md5.encode()).hexdigest()
        stretch_val -= 1
    return md5

otps = 0
potentials = {}
index = 0

def print_hash(hash):
    sys.stdout.write(f"{hash}\r")


os.system("cls")
sys.stdout.write("--------------SOTP--------------\n")
while True:
    hash = hash_string(f"{SALT}{index}", KEY_STRETCH)
    print_hash(hash)
    for i in range(len(hash) - 4):
        fragment = hash[i : i + 5]
        if len(set(fragment)) == 1:
            mark_to_pop = []
            for p in potentials:
                if potentials[p]["pattern"][0] == fragment[0]:
                    otps += 1
                    itp = potentials[p]["index"]
                    sys.stdout.write(f"{p} {itp}\n")
                    if otps == 64:
                        sys.stdout.write("-------------ENDKEY-------------\n")
                        exit()
                    mark_to_pop.append(p)
            for p in mark_to_pop:
                potentials.pop(p)

    for i in range(len(hash) - 2):
        fragment = hash[i : i + 3]
        if len(set(fragment)) == 1:
            potentials[hash] = {"pattern" : fragment[0], "age" : 0, "index" : index }
            break

    index += 1
    mark_to_pop = []
    for p in potentials:
        potentials[p]["age"] += 1
        if potentials[p]["age"] > 1000:
            mark_to_pop.append(p)
    for p in mark_to_pop:
        potentials.pop(p)