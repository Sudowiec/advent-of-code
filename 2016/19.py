NUMBER_OF_ELVES = 3017957

elves = {}
for elf_number in range(NUMBER_OF_ELVES):
    next = elf_number + 1 if elf_number + 1 != NUMBER_OF_ELVES else 0
    elves[elf_number] = {"next" : next}

current_elf = 0
while len(elves) > 1:
    steal_from = elves[current_elf]["next"]
    next = elves[steal_from]["next"]
    elves[current_elf]["next"] = next
    current_elf = elves[current_elf]["next"]
    elves.pop(steal_from)
print(list(elves.keys())[0] + 1)