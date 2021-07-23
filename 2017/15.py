ASTART = 65
BSTART = 8921
FACTORA = 16807
FACTORB = 48271
DIVISION = 2147483647

vala = ASTART
valb = BSTART
counter = 0
for i in range(40000000):
    tocount = True
    vala = (vala * FACTORA) % DIVISION
    valb = (valb * FACTORB) % DIVISION
    valbina = bin(vala)[2:]
    valbinb = bin(valb)[2:]
print(counter)