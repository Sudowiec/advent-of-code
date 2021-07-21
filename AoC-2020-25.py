subj = 7
primal = 20201227

public_card = 15733400
public_door = 6408062

loopsize_card = 0
num = 1
while True:
    loopsize_card += 1
    num *= subj
    num %= primal
    if num == public_card:
        break
print(loopsize_card)

loopsize_door = 0
num = 1
while True:
    loopsize_door += 1
    num *= subj
    num %= primal
    if num == public_door:
        break
print(loopsize_door)

key_card = 1
for i in range(loopsize_door):
    key_card *= public_card
    key_card %= primal
print(key_card)

key_door = 1
for i in range(loopsize_card):
    key_door *= public_door
    key_door %= primal
print(key_door)