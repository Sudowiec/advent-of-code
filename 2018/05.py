polymer = input()
og_letter_list = list(polymer)
shortest_pol = 50000

for letter in range(ord("A"), ord("Z") + 1):
    letter_list = list((filter(lambda x: chr(letter) not in x, og_letter_list)))
    letter_list = list((filter(lambda x: chr(letter + 32) not in x, letter_list)))
    while True:
        changed = False
        j = 0
        dj = 1
        for i in range(1, len(letter_list)):
            if abs(ord(letter_list[i]) - ord(letter_list[j])) == 32:
                letter_list[i] = '_'
                letter_list[j] = '_'
                changed = True
                dj = -1
            elif changed:
                dj = 1
                j = i - 1
            j += dj
        letter_list = list((filter(lambda x: '_' not in x, letter_list)))
        if not changed:
            break
    print(chr(letter), len(letter_list))
    if len(letter_list) < shortest_pol:
        shortest_pol = len(letter_list)
print(shortest_pol)