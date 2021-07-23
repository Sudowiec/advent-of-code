import re
input = "vzbxkghb"
print(input)

gcarry = 0
def incx(mobj):
    global gcarry
    a = mobj.group(1)
    n = ord(a) + gcarry
    if n > ord('z'):
        n = ord('a')
        gcarry = 1
    else:
        gcarry = 0
    a = chr(n)
    return a

def increase(password):
    global gcarry
    gcarry = 1
    p = password[::-1]
    p = re.sub(r"(.)", incx, p)
    return p[::-1]

def increaseold(password):
    lpassword = list(password)
    num_password = []
    for i in password:
        num_password.append(ord(i) - 96)
    num_password.reverse()
    carry = 0
    num_password[0] += 1
    for i in range(len(num_password)):
        num_password[i] += carry
        carry = 0
        if num_password[i] > 26:
            carry = 1
            num_password[i] = 1
    num_password.reverse()
    lpassword = []
    for i in num_password:
        lpassword.append(chr(i + 96))
    return("".join(lpassword))


def seeker(mobj):
    if mobj.group(1) != mobj.group(2):
        return "X"


while True:
    input = increase(input)
    # print(input)
    if re.search(r"(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)", input):
        if not re.search(r"([iol])", input):
            if "X" in re.sub(r"([a-z])\1.*([a-z])\2", seeker, input):
                print(input)
                # exit(0)
