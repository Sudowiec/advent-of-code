parts = []
while True:
    try:
        parts.append(list(map(int, input().split("/"))))
    except EOFError:
        break
print(parts)

def countStrength(bridge):
    s = 0
    for i in bridge:
        s += i[0] + i[1]
    return s

maxlen = 0
bridges = []

def build(pin, bridge, length):
    global maxlen
    for part in parts:
        if part not in bridge and pin in part:
            bridge.append(part)
            bridges.append([countStrength(bridge), length])
            if length > maxlen:
                maxlen = length
            lfPin = part[0] if part[1] == pin else part[1]
            build(lfPin, bridge, length + 1)
    if len(bridge) > 0:
        bridge.pop()

build(0, [], 1)
for i in bridges:
    if i[1] == maxlen:
        print(i)