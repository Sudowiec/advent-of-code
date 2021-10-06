recipes = "919901"

score = "37"
elf_one = 0
elf_two = 1
while recipes not in score[-7:]:
    score += str(int(score[elf_one]) + int(score[elf_two]))
    elf_one = (elf_one + int(score[elf_one]) + 1) % len(score)
    elf_two = (elf_two + int(score[elf_two]) + 1) % len(score)

print("Part 1:", score[int(recipes):int(recipes)+10])
print("Part 2:", score.index(recipes))