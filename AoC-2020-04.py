import re
passports = []
passport = {}
match = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
while True:
    try:
        inp = input()
    except EOFError:
        passports.append(passport)
        passport = {}
        break
    if inp == "":
        passports.append(passport)
        passport = {}
    else:
        mo = re.findall(r"(byr|iyr|eyr|hgt|hcl|ecl|pid):(\S+)", inp)
        for i in range(len(mo)):
            passport[mo[i][0]] = mo[i][1]

num = 0
for i in passports:
    valid = True
    if "ecl" in i:
        if not re.match(r"(amb|blu|brn|gry|grn|hzl|oth)", i["ecl"]):
            valid = False
    else:
        valid = False

    if "hcl" in i:
        if not re.match(r"#[0-9a-f]{6}", i["hcl"]):
            valid = False
    else:
        valid = False

    if "pid" in i:
        if not re.match(r"\d{9}$", i["pid"]):
            valid = False
    else:
        valid = False

    if "eyr" in i:
        if not re.match(r"(202\d|2030)", i["eyr"]):
            valid = False
    else:
        valid = False

    if "iyr" in i:
        if not re.match(r"(201\d|2020)", i["iyr"]):
            valid = False
    else:
        valid = False

    if "byr" in i:
        if not re.match(r"(19[2-9]\d|200[0-2])", i["byr"]):
            valid = False
    else:
        valid = False

    if "hgt" in i:
        if not re.match(r"(1[5-8]\dcm|19[0-3]cm|59in|6\din|7[0-6]in)", i["hgt"]):
            valid = False
    else:
        valid = False

    if valid:
        num += 1
        print(num, i["pid"])

print(num)
