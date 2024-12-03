import copy

FILE_NAME = "2024/02.txt"
FILE_LENGTH = 1000
PART = 2

def check_safeness(first, second):
    diff = first - second 
    if abs(diff) < 1 or abs(diff) > 3:
        return False, None
    return True, (diff > 0)
    
f = open(FILE_NAME, "r")
number_of_safes = 0
for line_number in range(FILE_LENGTH):
    level_reading = list(map(int, f.readline().split(" ")))
    num_of_levels_to_remove = 1 if PART == 1 else len(level_reading)
    for skipped_index in range(num_of_levels_to_remove):
        current_level_reading = copy.deepcopy(level_reading)
        if PART == 2:
            current_level_reading.pop(skipped_index)
        is_safe, is_beginning_increasing = check_safeness(current_level_reading[0], current_level_reading[1])
        if not is_safe:
            continue  

        is_all_safe = True
        for i in range(1, len(current_level_reading) - 1):
            is_safe, is_increasing = check_safeness(current_level_reading[i], current_level_reading[i + 1])
            if not is_safe or (is_beginning_increasing != is_increasing):
                is_all_safe = False
                break

        if is_all_safe:
            number_of_safes += 1
            break
print(number_of_safes)

