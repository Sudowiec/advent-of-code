import copy
f = open("2022/13.txt")
flist = []

global a
global b
def analyzeString(string, startIndx):
    arr = []
    global a;
    a = startIndx
    global b;
    b = startIndx + 1
    while True:
        if string[b] == ",":
            ta = string[a + 1:b]
            if ta == "":
                a += 1
                b += 1
                continue
            arr.append(int(ta))
            a = b
            b += 1
            continue
        elif string[b] == "[":
            a = b
            b += 1
            arr.append(analyzeString(string, a))
        elif string[b] == "]":
            ta = string[a + 1:b]
            if not ta == "":
                arr.append(int(ta))
            a = b
            b += 1
            return arr
        else:
            b += 1 

while True:
    l = f.readline()
    if l == "":
        break
    l = l.strip()
    flist.append(analyzeString(l, 0))
    flist.append(analyzeString(f.readline().strip(), 0))
    f.readline()
flist.append([[2]])
flist.append([[6]])
size = len(flist)
def convToArr(num):
    tmpl = []
    tmpl.append(num)
    return tmpl

def compareArrays(inp1, inp2):
    arr1 = copy.deepcopy(inp1)
    arr2 = copy.deepcopy(inp2)
    s = max([len(arr1), len(arr2)])
    i = 0
    while i < s:
        try:
            a = arr1[i]
        except IndexError:
            return 2
        try:
            a = arr2[i]
        except IndexError:
            return 0
        if type(arr1[i]) == type(arr2[i]):
            if type(arr1[i]) == int:
                if arr1[i] > arr2[i]:
                    return 0
                elif arr1[i] < arr2[i]:
                    return 2
                else:
                    i += 1
                    continue
            else:
                res = compareArrays(arr1[i], arr2[i])
                if res == 1:
                    i += 1
                    continue
                else:
                    return res
        else:
            if type(arr1[i]) == int:
                arr1[i] = convToArr(arr1[i])
            else:
                arr2[i] = convToArr(arr2[i])
            i -= 1
        i += 1
    return 1

print()
def sortlist(arr):
    for n in range(len(arr)-1, 0, -1):
        for i in range(n):
            if compareArrays(arr[i], arr[i + 1]) == 0:
                tmp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = tmp
sortlist(flist)
print("Decoder key", (flist.index([[6]]) + 1) * (flist.index([[2]]) + 1))