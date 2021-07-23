import json
inp = input()
jinp = json.loads(inp)
print(jinp)

def countsth(given_list):
    sumup = 0
    if isinstance(given_list, list):
        for i in given_list:
            if isinstance(i, list) or isinstance(i, dict):
                sumup += countsth(i)
            elif isinstance(i, int):
                sumup += i

        return(sumup)
    elif isinstance(given_list, dict):
        for i in given_list:
            if isinstance(given_list[i], list) or isinstance(given_list[i], dict):
                sumup += countsth(given_list[i])
            elif isinstance(given_list[i], int):
                sumup += given_list[i]
            elif given_list[i] == "red":
                return(0)

        return(sumup)
print(jinp)
print(countsth(jinp))