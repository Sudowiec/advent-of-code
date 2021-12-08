counter = 0
while True:
    try:
        maininp = input().split("|")
    except EOFError:
        break
    inp = maininp[0].split(" ")
    inp.pop()
    outp = maininp[1].split(" ")
    outp.pop(0)

    for i in outp:
        l = len(i)
        if l in [2, 3, 4, 7]:
            counter += 1
print(counter)
