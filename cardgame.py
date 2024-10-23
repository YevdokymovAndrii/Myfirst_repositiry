import random, string, time, os


def make_list(value):
    new_list = []
    for char in value:
        new_list.append(char)
    return new_list


def generate_field(characters):
    characters *= 2
    field = []
    for i in range(4):
        buffer_row = []
        for j in range(4):
            chosen_symbol = random.choice(characters)
            buffer_row.append(chosen_symbol)
            del characters[characters.index(chosen_symbol)]
        field.append(buffer_row)
    return field


def make_move(counter, closed_field1):
    coords = []
    print_field(closed_field)
    for i in range(2):
        coordinate = input(f"Please, enter coordinate of the {i + 1} card - ")
        while True:
            if coordinate.isnumeric() and 11 <= int(coordinate) <= 44 and closed_field[int(coordinate) // 10 - 1][
                int(coordinate) % 10 - 1] == "#":
                if len(coords) == 2:
                    if (coords[0] + 1) * 10 + coords[1] + 1 == int(coordinate):
                        coordinate = input("Please, enter valid value - ")
                    else:
                        break
                elif len(coords) == 0:
                    break
            else:
                coordinate = input("Please, enter valid value - ")
        coordinate = int(coordinate)
        coords.append(coordinate // 10 - 1)
        coords.append(coordinate % 10 - 1)
    showed_symbols_field = closed_field
    for i in range(4):
        for j in range(4):
            if showed_symbols_field[i][j] != "#":
                showed_symbols_field[i][j] = closed_field1[i][j]
    showed_symbols_field[coords[0]][coords[1]] = opened_field[coords[0]][coords[1]]
    showed_symbols_field[coords[2]][coords[3]] = opened_field[coords[2]][coords[3]]
    os.system("cls")

    if showed_symbols_field[coords[0]][coords[1]] == showed_symbols_field[coords[2]][coords[3]]:
        closed_field[coords[0]][coords[1]] = showed_symbols_field[coords[0]][coords[1]]
        closed_field[coords[2]][coords[3]] = showed_symbols_field[coords[2]][coords[3]]
    else:
        print_field(showed_symbols_field)
        time.sleep(2)
        os.system("cls")
        closed_field[coords[0]][coords[1]] = "#"
        closed_field[coords[2]][coords[3]] = "#"
    counter += 1
    return closed_field1, counter


def print_field(field):
    print("  1 2 3 4")
    for i in range(4):
        print(f"{i + 1}", end=" ")
        print(*field[i])

LETTERS = string.ascii_lowercase
NUMBERS = "0123456789"
SPECIAL_SYMBOLS = "!@?$%^&*"
count_moves = 0
closed_field = [["#" for _ in range(4)] for _ in range(4)]
print("Hello, this game is designed to train you memory")
print("You can use existing sets of symbols - numbers, letters or special symbols, to use them type n, l, or ss respectevily")
print("Also you can use your own set of symbols, simply by entering them")


symbols = input("Please, enter set of symbols you want to train your memory with - ").split(" ")
valid_length = True
while True:
    for i in symbols:
        if len(i) != 1:
            valid_length = False
            break
        else:
            valid_length = True
    if len(symbols) == 8 and valid_length:
        start_validation = False
    elif len(symbols) == 1 and (symbols[0] == "n" or symbols[0] == "l" or symbols[0] == "ss"):
        symbols = symbols[0]
        break
    else:
        symbols = input("Please, enter valid data - ").split(" ")

symbol_set = ""
if len(symbols) < 8:
    if symbols == "n":
        symbol_set = NUMBERS
        deleted_symbols = random.randint(0, 9)
        symbol_set = symbol_set.replace(str(deleted_symbols), "")
    elif symbols == "ss":
        symbol_set = SPECIAL_SYMBOLS
    elif symbols == "l":
        while len(symbol_set) < 8:
            added_symbol = random.choice(LETTERS)
            if not added_symbol in symbol_set:
                symbol_set += added_symbol
            else:
                added_symbol = random.choice(LETTERS)
else:
    symbol_set = ""
    for i in symbols:
        symbol_set += i
symbol_set = make_list(symbol_set)
print()
print("Your set of symbols for this game is ", end = " ")

for i in symbol_set:
    print(i, end = " ")
print()

opened_field = generate_field(symbol_set)


while True:
    count = 0
    for i in closed_field:
        count += i.count("#")
    if count == 0:
        break
    else:
        closed_field, count_moves = make_move(count_moves, closed_field)
print(f"Congratulations! You won the game in {count_moves} moves")
