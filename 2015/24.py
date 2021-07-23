import collections
import math
import itertools
packages = []
while True:
    try:
        packages.append(int(input()))
    except EOFError:
        break
low_len = int(len(packages) / 4)
main_sum = sum(packages)
lf = int(main_sum / 4)

qes = collections.defaultdict(lambda : 999999999999999999999999999)
for i in range(1, low_len + 1):
    ls = list(itertools.combinations(packages, i))
    for j in ls:
        if sum(j) == lf:
            print(j, math.prod(j))
            if math.prod(j) < qes[i]:
                qes[i] = math.prod(j)
print(qes)


