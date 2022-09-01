# попытка номер 4
empty = '-'
cross = 'X'
zero = 'O'
FIELD = {}
for i in range(1,4):
    for j in range(1,4):
        FIELD [int(str(i)+str(j))] = empty
def graphic_field():
    print(f'   1  2  3')
    print(f' 1 {FIELD.get(11)}  {FIELD.get(12)}  {FIELD.get(13)}')
    print(f' 2 {FIELD.get(21)}  {FIELD.get(22)}  {FIELD.get(23)}')
    print(f' 3 {FIELD.get(31)}  {FIELD.get(32)}  {FIELD.get(33)}')
def you_move():
     move = 0
     while not (move in FIELD) :
        move = int(input('Введите Ваш ход : '))
        if (not (move in FIELD)):
             print('Нет такого поля!')
        elif FIELD[move] == cross or FIELD[move] == zero:
             print('Поле занято!')
             move = 0
     FIELD [move] = cross
     return move
def computer_move(coordinate):
    if FIELD [22] == empty:
        FIELD[22] = zero
        return
    list_column =[]
    list_line = []
    list_diagonal = []
    move_computer = 0
    column = int(str(coordinate(0)))
    line = int(str(coordinate(1)))
    for i in range(1,4):
        list_line.append(FIELD[int(str(i)+str(line))])
        list_column.append(FIELD[int(str(column) + str(i))])
        if column == line != 2:
            list_diagonal.append(FIELD[int(str(i)+str(i))])
        elif column != 2 and line != 2 and column != line:
            list_diagonal.append(FIELD[int(str(i)+str(i))])
    match_checking ={}



    
graphic_field()
you_move()
graphic_field()
