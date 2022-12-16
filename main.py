from support import *

EMPTY = '-'
CROSS = 'X'
ZERO = '0'
field = {convert_digit_num(y, x): EMPTY for x in range(1, 4) for y in range(1, 4)}
CORNER = ['11', '13', '33', '31']
ERROR = 'Ошибка ввода!!!'


def print_field():
    n = 0
    print(f'  1|2|3')
    for i in range(1, 4):
        print(f'{i}|', end='')
        for m in range(0, 3):
            print(f'{list(map(list, field.items()))[n][1]}|', end='')
            n += 1
        print()

def change_character(num, sym):
    for key, s in field.items():
        if key == num:
            field[key] = sym
            break


def player_turn():
    cord = input('Введите кординаты: ')
    while not check_num(cord) or not check_sym(field, cord):
        print(ERROR)
        cord = input('Введите кординаты: ')
    change_character(cord, CROSS)
    print_field()
    return cord

def computer_tur(prevHuman, prevComp):
    print('Ход компьютера :')
    cordFlag = [None, False]
    if field['22'] == EMPTY:
        change_character('22', ZERO)
        cordFlag[0] = '22'
    else:
        if prevComp and ((cordFlag := check_line(field, prevComp, ZERO)) or
                         (cordFlag := check_line(field, prevHuman, CROSS))):
            change_character(cordFlag[0], ZERO)
            if cordFlag[1]:
                print('Компьютер победил!')
                print_field()
                return 'win'
        else:
            if (field[CORNER[0]] == field[CORNER[2]] and field[CORNER[0]] == CROSS) or\
                (field[CORNER[1]] == field[CORNER[3]] and field[CORNER[1]] == CROSS):
                for key, a in field.items():
                    if a == EMPTY and not (key in CORNER):
                        change_character(key, ZERO)
                        print_field()
                        return key
            for c in CORNER:
                if field[c] == EMPTY:
                    change_character(c, ZERO)
                    cordFlag = [c, False]
                    break

    if cordFlag is None:
        cordFlag = [find_empty(field), False]
        change_character(cordFlag[0], ZERO)

    print_field()
    return cordFlag[0]

def clear_field():
    for key, sim in field.items():
        field[key] = EMPTY