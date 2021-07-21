programs = "abcdefghijklmnop"
programs = list(programs)
print(programs)
instructions = input().split(",")
cache = {}

# stage 2
num = 1000000000 % 60

for j in range(num):
    for ins in instructions:
        # spin
        if ins[0] == "s":
            ins = int(ins[1:])
            for i in range(ins):
                last = programs.pop()
                programs.reverse()
                programs.append(last)
                programs.reverse()
        # exchange
        elif ins[0] == "x":
            ins = list(map(int, ins[1:].split("/")))
            a = programs[ins[0]]
            programs[ins[0]] = programs[ins[1]]
            programs[ins[1]] = a
        # partner
        elif ins[0] == "p":
            ins = ins[1:].split("/")
            posone = programs.index(ins[0])
            postwo = programs.index(ins[1])
            a = programs[posone]
            programs[posone] = programs[postwo]
            programs[postwo] = a
    strprograms = "".join(programs)
    # this proves the "60 dances cycle" theory
    # if j%60 == 0:
    #     print(strprograms)
    # if strprograms in cache:
    #     print(strprograms, j)
    # else:
    #     cache[strprograms] = 1
print(strprograms)
