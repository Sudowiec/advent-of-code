scoreTable = { "A" : 1, "B" : 2, "C" : 3, "X" : 0, "Y" : 3, "Z" : 6}
totalScore = 0
# A -> B
# B -> C
# C -> A

while True:
    try:
        inp = input().split(" ")
    except EOFError:
        break
    
    totalScore += scoreTable[inp[1]]

    if inp[1] == "Y": # draw
        totalScore += scoreTable[inp[0]]
    elif inp[1] == "Z": # win
        totalScore += scoreTable[inp[0]] + 1 if scoreTable[inp[0]] != 3 else 1
    elif inp[1] == "X": # lose
        totalScore += scoreTable[inp[0]] - 1 if scoreTable[inp[0]] != 1 else 3

print(totalScore)