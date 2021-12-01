prevnum = int(input())
counter = 0
while True:
    try:
        num = int(input())
    except EOFError:
        break
    if num > prevnum:
        counter += 1
    prevnum = num
print(counter)