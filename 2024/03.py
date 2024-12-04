import re
FILE_NAME = "2024/03.txt"
FILE_SIZE = 6

sum = 0
f = open(FILE_NAME, "r")
for line_number in range(FILE_SIZE):
    inp = f.readline()
    findings = re.findall("mul[(]\d{1,3},\d{1,3}[)]", inp)
    for mul in findings:
        numbers = list(map(int, re.findall("\d{1,3}", mul)))
        sum += numbers[0] * numbers[1]
print(sum)