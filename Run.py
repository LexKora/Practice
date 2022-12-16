from main import *
moves_ = [None, None]
gameFlag = 1
print('Здравствуйте! Это игра "Крестики нолики".')
while int(gameFlag):
    print('Вводите двухзначное число где первая цифра будет вертикаль а вторая горизонталь.')
    print_field()
    countRaund = 0
    while countRaund < 10:
        moves_[0] = player_turn()
        countRaund +=1
        moves_[1] = computer_tur(moves_[0], moves_[1])
        if moves_[1] == 'win':
            break
        countRaund += 1
        if countRaund == 10:
            print('Ничья.')

    while int(gameFlag):
        gameFlag = input('Ещё одна партия?(0 - Нет, 1 - Да)')
        if gameFlag == '1' or gameFlag == '0':
            break
        else:
            print('Неверный ввод!!!')
            gameFlag = 1
    clear_field()

print('Всего хорошего!')