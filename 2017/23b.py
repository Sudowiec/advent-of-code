inp = 81
beg = inp * 100 + 100000
end = beg + 17000
result = 1

def isPrime(num):
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True

for i in range(beg, end, 17):
    if (not isPrime(i)):
        result += 1

print(result)