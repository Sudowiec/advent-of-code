START_ROW = ".^^^.^.^^^.^.......^^.^^^^.^^^^..^^^^^.^.^^^..^^.^.^^..^.^..^^...^.^^.^^^...^^.^.^^^..^^^^.....^...."
ROWS_TO_ASSESS = 400000
ROW_LENGTH = len(START_ROW)

def tell_tile(left, right):
    if left != right:
        return "^"
    return "."

number_of_safes = 0
current_row = START_ROW
for row_number in range(ROWS_TO_ASSESS):
    print(current_row, row_number + 1)
    number_of_safes += current_row.count(".")
    new_row = ""
    for tile_number in range(ROW_LENGTH):
        left = current_row[tile_number - 1] if tile_number > 0 else "."
        right = current_row[tile_number + 1] if tile_number < ROW_LENGTH - 1 else "."
        new_row += tell_tile(left, right)
    current_row = new_row
print(number_of_safes)