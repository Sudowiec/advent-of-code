inps = []
while True:
    try:
        inps.append(int(input()))
    except EOFError:
        break

# for i in inps:
#     for j in inps:
#         for k in inps:
#             if i + j + k == 2020:
#                 print(i*j*k)
#                 break

for i in range(len(inps)):
    for j in range(i, len(inps)):
        for k in range(j, len(inps)):
            if inps[i] + inps[j] + inps[k] == 2020:
                print(inps[i]*inps[j]*inps[k])
                break