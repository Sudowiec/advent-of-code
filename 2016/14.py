import hashlib

salt = "ngcjuoqr"

otps = 0
potentials = {}
index = 0
while True:
    hash = hashlib.md5(f"{salt}{index}".encode()).hexdigest()
    for i in range(len(hash) - 4):
        fragment = hash[i : i + 5]
        if len(set(fragment)) == 1:
            mark_to_pop = []
            for p in potentials:
                if potentials[p]["pattern"][0] == fragment[0]:
                    otps += 1
                    print(otps, p, potentials[p]["index"])
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