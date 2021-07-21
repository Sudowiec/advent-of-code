import copy
boss_stats = {"hp" : 109, "dmg" : 8, "arm" : 2}
player_stats = {"hp" : 100, "dmg" : 0, "arm" : 0}

# fight function
def fight(boss, player):
    strike = 0
    while True:
        if strike % 2 == 0:
            # player attacks
            attack = player["dmg"] - boss["arm"]
            if attack < 1:
                attack = 1
            boss["hp"] -= attack
        else:
            # boss attacks
            attack = boss["dmg"] - player["arm"]
            if attack < 1:
                attack = 1
            player["hp"] -= attack
        if player["hp"] < 0 or boss["hp"] < 0:
            break
        strike += 1
    if strike % 2 == 0:
        return "player"
    else:
        return "boss"

# shop implementation
shop = { "weapons" : [], "armor" : [], "rings" : [] }
num_of_assets = {"weapons" : 0, "armor" : 0, "rings" : 0}

accessory = ""
while True:
    try:
        inp = input().split(" ")
    except EOFError:
        break
    if len(inp) == 1:
        accessory = inp[0]
        id = 1
        continue

    thing = {"id" : id, "name": inp[0], "cost" : int(inp[1]), "dmg" : int(inp[2]), "arm" : int(inp[3])}
    shop[accessory].append(thing)
    id += 1
    num_of_assets[accessory] += 1
print(shop)
print(num_of_assets)

# creating permutations of IDs and simulating the fights
player_inv = {"weapon" : -1, "armor" : -1, "lring" : -1, "rring" : -1}
highest_cost = 0
for wp in range(1, num_of_assets["weapons"] + 1):
    for arm in range(num_of_assets["armor"] + 1):
        for rr in range(num_of_assets["rings"] + 1):
            for lr in range(num_of_assets["rings"] + 1):
                if rr == lr:
                    if rr != 0 and lr != 0:
                        continue

                # counting cost and preparing stats
                cost = 0
                defense = 0
                offense = 0
                for i in shop["weapons"]:
                    if i["id"] == wp:
                        cost += i["cost"]
                        defense += i["arm"]
                        offense += i["dmg"]
                        break
                if arm != 0:
                    for i in shop["armor"]:
                        if i["id"] == arm:
                            cost += i["cost"]
                            defense += i["arm"]
                            offense += i["dmg"]
                            break
                if rr != 0:
                    for i in shop["rings"]:
                        if i["id"] == rr:
                            cost += i["cost"]
                            defense += i["arm"]
                            offense += i["dmg"]
                            break
                if lr != 0:
                    for i in shop["rings"]:
                        if i["id"] == lr:
                            cost += i["cost"]
                            defense += i["arm"]
                            offense += i["dmg"]
                            break
                if cost <= highest_cost:
                    continue
                actual_player_stats = copy.deepcopy(player_stats)
                actual_boss_stats = copy.deepcopy(boss_stats)
                actual_player_stats["dmg"] += offense
                actual_player_stats["arm"] += defense

                # FIGHT!
                winner = fight(actual_boss_stats, actual_player_stats)
                if winner == "boss":
                    highest_cost = cost
print(highest_cost)

