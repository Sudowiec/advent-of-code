import re
nice = 0
nice_two = 0
while True:
    try:
        inp = input()
    except EOFError:
        print(nice, nice_two)
        break
    # It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    if re.search(r"([aeiou].*){3}", inp) != None:
        # It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
        if re.search(r"([a-z])\1", inp) != None:
            # It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
            if re.search(r"(ab|cd|pq|xy)", inp) == None:
                nice += 1

    # It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy)
    # or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
    if re.search(r"([a-z][a-z]).*\1", inp) != None:
        # It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
        if re.search(r"([a-z]).\1", inp) != None:
            nice_two += 1