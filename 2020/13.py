minute = int(input())
busses = list(set(input().split(",")))
busses.remove("x")
busses = list(map(int, busses))
print(minute, busses)

rests = {}
for i in busses:
    modulo = minute % i
    rests[i] = i - modulo
lowval = min(rests.values())
id = 0
for i in rests:
    if rests[i] == lowval:
        id = i
print(lowval * id)
