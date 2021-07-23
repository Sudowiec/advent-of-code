from collections import Counter
node = {"marble": 0}
node["next"] = node
node["prev"] = node

players_num = 426
last_marble = 7205800
curr_player = 0
score = Counter()
for i in range(1, last_marble):
    # indx = node
    # for j in range(i):
    #     print(str(indx["marble"]) + " ", end='')
    #     indx = indx["next"]
    # print(' ')

    if i % 23 == 0:
        score[curr_player] += i
        for j in range(7):
            node = node["prev"]
        score[curr_player] += node["marble"]
        node["prev"]["next"] = node["next"]
        node["next"]["prev"] = node["prev"]
        node = node["next"]
    else:
        node = node["next"]
        new_node = {"marble": i}
        new_node["prev"] = node
        new_node["next"] = node["next"]
        node["next"]["prev"] = new_node
        node["next"] = new_node
        node = new_node
    curr_player = (curr_player + 1) % players_num
print(max(score.values()))