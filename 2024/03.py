import re
FILE_NAME = "2024/03.txt"
FILE_SIZE = 6
PART = 2

REGEX_FIND_MULS = ["mul\\(\d{1,3},\d{1,3}\\)", "mul\\(\d{1,3},\d{1,3}\\)|do.{0,3}\\(\\)"]

sum = 0
f = open(FILE_NAME, "r")
do = True
for line_number in range(FILE_SIZE):
    inp = f.readline()
    findings = re.findall(REGEX_FIND_MULS[PART - 1], inp)
    for mul in findings:
        if mul[0] == "d":
            do = False if mul[2] == "n" else True
            continue
        if do:
            numbers = list(map(int, re.findall("\d{1,3}", mul)))
            sum += numbers[0] * numbers[1]
print(sum)