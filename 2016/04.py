from collections import defaultdict
FLENGTH = 1066
ALPHABET = "abcdefghijklmnopqrstuvwxyz"

sum = 0
f = open("04.txt")
for i in range(FLENGTH):
    l = f.readline().split("-")
    checksum = l[-1].split("[")[1].strip()[:-1]
    secId = int(l[-1].split("[")[0])
    enc = l[:-1]
    
    count = defaultdict(lambda : 0)
    for i in enc:
        for j in i:
            count[j] += 1

    st = defaultdict(lambda : [])
    for w in sorted(count, key=count.get, reverse=True):
        st[count[w]].append(w)
    for w in st:
        st[w] = sorted(st[w])
    
    fin = []
    for j in st.values():
        for k in j:
            fin.append(k)
    fin = "".join(fin[:5])
    
    if fin == checksum:
        sentence = list(" ".join(l[:-1]))
        for letter_ind in range(len(sentence)):
            if sentence[letter_ind] == " ":
                continue
            sentence[letter_ind] = ALPHABET[(ALPHABET.index(sentence[letter_ind]) + secId) % 26]
        print(secId, "".join(sentence))