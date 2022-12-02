scoreTable = { "A" : 1, "B" : 2, "C" : 3, "X" : 1, "Y" : 2, "Z" : 3 }
totalScore = 0

while True:
    try:
        inp = input().split(" ")
    except EOFError:
        break
    
    totalScore += scoreTable[inp[1]]

    resultCheck = scoreTable[inp[0]] - scoreTable[inp[1]]
    
    if resultCheck == -1 or resultCheck == 2: # win
        totalScore += 6
    elif resultCheck == 0: # draw
        totalScore += 3

print(totalScore)