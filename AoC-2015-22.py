import copy
player_temp = {"hp" : 50, "mp" : 500, "arm" : 0, "armor left" : 0, "recharge left" : 0}
boss_temp = {"hp" : 55, "dmg" : 8, "arm" : 0, "poison left" : 0}
# 0 Magic Missile costs 53 mana. It instantly does 4 damage.
# 1 Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
# 2 Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
# 3 Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
# 4 Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana.
spells = [{"id" : 0, "cost" : 53},
          {"id" : 1, "cost" : 73},
          {"id" : 2, "cost" : 113},
          {"id" : 3, "cost" : 173},
          {"id" : 4, "cost" : 229},
          {"id" : 5, "cost" : 0}]
spent_mp_list = []
lowest_spent = 999999

def effect_manager(player, boss):
    # managing player effects

    if player["armor left"] > 0:
        player["arm"] = 7
    if player["armor left"] == 0:
        player["arm"] = 0
    if player["recharge left"] > 0:
        player["mp"] += 101
    player["armor left"] -= 1
    player["recharge left"] -= 1

    # managing boss effects
    if boss["poison left"] > 0:
        boss["hp"] -= 3
    boss["poison left"] -= 1

status = {}
def fight(preplayer, preboss, prespent_mp, lvl):
    global spells
    global spent_mp_list
    global lowest_spent
    # spell tree managing
    for i in spells:
        spent_mp = prespent_mp
        player = copy.deepcopy(preplayer)
        boss = copy.deepcopy(preboss)
        effect_manager(player, boss)
        if player["mp"] < i["cost"]:
            continue
        player["hp"] -= 1
        if player["hp"] <= 0:
            continue
        # magic missle
        if i["id"] == 0:
            boss["hp"] -= 4
            player["mp"] -= 53
            spent_mp += 53
        # drain
        elif i["id"] == 1:
            boss["hp"] -= 2
            player["hp"] += 2
            player["mp"] -= 73
            spent_mp += 73
        # shield
        elif i["id"] == 2:
            if player["armor left"] <= 0:
                player["armor left"] = 6
                player["mp"] -= 113
                spent_mp += 113
            else:
                continue
        # poison
        elif i["id"] == 3:
            if boss["poison left"] <= 0:
                boss["poison left"] = 6
                player["mp"] -= 173
                spent_mp += 173
            else:
                continue
        # recharge
        elif i["id"] == 4:
            if player["recharge left"] <= 0:
                player["recharge left"] = 5
                player["mp"] -= 229
                spent_mp += 229
            else:
                continue
        # player ran out of mp and loses the fight
        elif i["id"] == 5:
            return

        status[lvl] = "plr = " + str(player["hp"]) + ", boss = " + str(boss["hp"]) + ",mp = " + str(player["mp"]) + ", used = " + str(spent_mp) + ", id = " + str(i["id"])

        # too_much mp optimalization
        if spent_mp >= lowest_spent:
            continue
        # player won
        effect_manager(player, boss)
        if boss["hp"] <= 0:
            lowest_spent = spent_mp
            print(lvl, lowest_spent)
            for j in range(lvl + 1):
                print(status[j])
            continue

        # boss strikes
        player["hp"] -= boss["dmg"] - player["arm"]

        # boss won
        if player["hp"] <= 0:
            continue

        # print(lvl)
        # r e c u r s i o n
        fight(player, boss, spent_mp, lvl + 1)

fight(player_temp, boss_temp, 0, 0)
print(lowest_spent)

