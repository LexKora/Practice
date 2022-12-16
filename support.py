import random

EMPTY = '-'

def check_num(num):
    if all(map(str.isdigit, num)) and len(num) == 2 \
            and 0 < convert_num_to_digit(num)[0] < 4 and 0 < convert_num_to_digit(num)[1] < 4:
        return True
    else:
        print('Неверный формат!!! ', end='')
        return False

def random_num(listok):
    if len(listok) == 1:
        return listok[0]
    else:
        listok[random.randint(len(listok))]
def convert_num_to_digit(n):
    a, b = int(list(n)[0]), int(list(n)[1])
    return a, b
def convert_digit_num(a, b):
    return str(a) + str(b)

def check_sym(field, n):
    if field[n] != '-':
        print('Клетка занята!!! ', end='')
        return False
    return True

def check_line(field, move, sym):
    cordFlag = None
    line1 = {}
    line2 = {}
    line3 = {}
    pool = [line1, line2, line3]

    cor1, cor2 = convert_num_to_digit(move)
    def add_meaning(olddict, newdict, a, b):
        key_ = convert_digit_num(a, b)
        newdict[key_] = olddict[key_]
    for i in range(1, 4):
        add_meaning(field, pool[0], cor1, i)
        add_meaning(field, pool[1], i, cor2)

        if cor1 == cor2:
            add_meaning(field, pool[2], i, i)
        if int(cor1)+int(cor2) == 4:
            add_meaning(field, pool[2], i, 4 - i)
    for line in pool:
        count = 0
        del_list = line.copy()
        if len(list(line)) == 0:
            break
        for key, s in line.items():
            if s == sym:
                count += 1
                del_list.pop(key)
            if count == 2 and list(del_list.items())[0][1] == EMPTY:
                cordFlag = [list(del_list.items())[0][0], False]
                if sym == '0':
                    cordFlag[1] = True
                return cordFlag
    return cordFlag

def find_empty(field):
    for key, s in field.items():
        if s == EMPTY:
            return key