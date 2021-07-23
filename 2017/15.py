ASTART = 679
BSTART = 771
FACTORA = 16807
FACTORB = 48271
DIVISION = 2147483647

vala = ASTART
valb = BSTART
counter = 0
to_compare_a = []
to_compare_b = []
while True:
    if len(to_compare_a) < 5000000:
        vala = (vala * FACTORA) % DIVISION
        if int(str(vala)[-2:]) % 4 == 0:
            to_compare_a.append(bin(vala)[-16:])
    if len(to_compare_b) < 5000000:
        valb = (valb * FACTORB) % DIVISION
        if int(str(valb)[-3:]) % 8 == 0:
            to_compare_b.append(bin(valb)[-16:])
    if len(to_compare_a) >= 5000000 and len(to_compare_b) >= 5000000:
        break


for i in range(5000000):
    if to_compare_a[i] == to_compare_b[i]:
        counter += 1
print(counter)