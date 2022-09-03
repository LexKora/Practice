# попытка номер 4
empty = '-'
cross = 'X'
zero = 'O'
flag = False
FIELD = {x: [empty] for x in (11, 12, 13, 21, 22, 23, 31, 32, 33)}
valid_filds = [{key: FIELD[key] for key, sim in FIELD.items() if list(str(key))[j] == str(i)} for i in range(1, 4)
               for j in range(0, 2)]
valid_filds.append({key: sim for key, sim in FIELD.items() if list(str(key))[0] == list(str(key))[1]})
valid_filds.append({key: sim for key, sim in FIELD.items() if int(list(str(key))[0]) +
                    int(list(str(key))[1]) == 4})

def graphic_field():
    print(f'   1  2  3')
    print(f' 1 {FIELD.get(11)[0]}  {FIELD.get(12)[0]}  {FIELD.get(13)[0]}')
    print(f' 2 {FIELD.get(21)[0]}  {FIELD.get(22)[0]}  {FIELD.get(23)[0]}')
    print(f' 3 {FIELD.get(31)[0]}  {FIELD.get(32)[0]}  {FIELD.get(33)[0]}')
def you_move():
     move = 0
     while not (move in FIELD):
        move = int(input('Введите Ваш ход : '))
        if (not (move in FIELD)):
             print('Нет такого поля!')
        elif FIELD[move][0] == cross or FIELD[move][0] == zero:
             print('Поле занято!')
             move = 0
     FIELD [move][0] = cross
     return move

def examination (kwargs , sym_ ):
    global flag
    if kwargs == None:
        kwargs = {}
    count = 0

    for key, sym in kwargs.items():
        if sym[0] == sym_:
            count += 1
        if count == 2:
            for key_, sym__ in kwargs.items():
                if sym__[0] == empty:
                    FIELD[key_][0] = zero
                    if sym_ == zero:
                        graphic_field()
                        print('Компьютер победил!')
                        exit(0)
                    flag = True
                    break

def computer_move():
    global flag
    flag = False
    if FIELD [22][0] == empty:
        FIELD[22][0] = zero
        return

    else:
        for field in valid_filds:
            if flag:
                break
            examination(field, zero)
        for field in valid_filds:
            if flag:
                break
            examination(field, cross)

        if not flag:
            for key__, sym___ in FIELD.items():
                if (int(list(str(key__))[0]) + int(list(str(key__))[1])) % 2 == 0 and sym___[0] == empty and \
                        (FIELD[11][0] != FIELD[33][0]) == cross and FIELD[13][0] == FIELD[31][0] == cross :
                    FIELD[key__][0] = zero
                    print('!!!')
                    flag = True
                    break

            for key__, sym___ in FIELD.items():
                if sym___[0] == empty and (int(list(str(key__))[0]) + int(list(str(key__))[1])) % 2 != 0 and\
                        not flag:
                    FIELD[key__][0] = zero
                    print('???')
                    break


play_move = 0
while play_move < 9:
    graphic_field()
    you_move()
    computer_move()
    play_move += 2
graphic_field()
print('Ничья')

