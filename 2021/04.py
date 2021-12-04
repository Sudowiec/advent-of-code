def boardcheck(board):
    for i in board:
        if i == ['#', '#', '#', '#', '#']:
            return True

    counter = 0
    for i in range(5):
        for j in board:
            if j[i] != '#':
                counter = 0
                break
            else:
                counter += 1
        if counter == 5:
            return True
    return False

numbers = list(map(int, input().split(",")))
input()
boards = []
board = []
while True:
    try:
        inp = input()
    except EOFError:
        boards.append(board)
        break
    if inp == "":
        boards.append(board)
        board = []
        continue
    inp = inp.split(" ")
    for i in inp:
        if i == "":
            inp.remove(i)
    board.append(list(map(int, inp)))
#print(boards)

foundwin = False
for num in numbers:
    for board in boards:
        for i in board:
            if num in i:
                board[board.index(i)][i.index(num)] = "#"
            if boardcheck(board):
                winner = board
                winnum = num
                foundwin = True
                break
        if foundwin:
            break
    if foundwin:
        break

sum = 0
for i in winner:
    for j in i:
        if j != "#":
            sum += j
print(sum)
print(winnum)
print(sum*winnum)

