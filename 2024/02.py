FILE_NAME = "2024/02.txt"
FILE_LENGTH = 1000

def check_safeness(first, second):
    diff = first - second 
    if abs(diff) < 1 or abs(diff) > 3:
        return False, None
    return True, (diff > 0)
    
f = open(FILE_NAME, "r")
number_of_safes = 0
for line_number in range(FILE_LENGTH):
    level_reading = list(map(int, f.readline().split(" ")))
    
    is_safe, is_beginning_increasing = check_safeness(level_reading[0], level_reading[1])
    if not is_safe:
        continue
    
    is_all_safe = True
    for i in range(1, len(level_reading) - 1):
        is_safe, is_increasing = check_safeness(level_reading[i], level_reading[i + 1])
        if not is_safe or (is_beginning_increasing != is_increasing):
            is_all_safe = False
            break
    if is_all_safe:
        number_of_safes += 1
print(number_of_safes)

