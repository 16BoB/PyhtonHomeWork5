# 2- Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет(или сколько вы зададите). Тот, кто берет последнюю конфету - проиграл.
# Предусмотрите последний ход, ибо там конфет остается меньше.

# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"
import random

def input_check_int_game():
    while True:
        try:
            input_num = int(input(f'Ввеите число от 1 до 28 включительно: '))
            if 0 < input_num <= shag and input_num <= col_candy:
                return input_num
            else:
                print('Вы ввели неправильное значение!')
        except ValueError:
            print('Вы ввели неправильное значение!')

while True:
    try:
        col_candy = int(input(f'Ввеите колличество конфет больше 1: '))
        if 1 < col_candy:
            break
        else:
            print('Вы ввели неправильное значение!')
    except ValueError:
        print('Вы ввели неправильное значение!')

while True:
    try:
        shag = int(input(f'Ввеите максимальное колличество конфет, минимально 1, которое можно брать, и не больше чем конфет всего: '))
        if 1 <= shag <= col_candy:
            break
        else:
            print('Вы ввели неправильное значение!')
    except ValueError:
        print('Вы ввели неправильное значение!')

first_player = random.randint(1, 2)
second_player = 2
if first_player == 2:
    second_player = 1

print(f"первым ходит {first_player}")
print(f"вторым ходит {second_player}")

while col_candy > 0:
    print(f'hod igroka {first_player}:')
    minus_candy = input_check_int_game()
    col_candy = col_candy - minus_candy
    print(f'Конфет осталось {col_candy}')
    if col_candy == 1:
        print(f'Проиграл игрок {first_player}!')
        break
    print(f'hod igroka {second_player}:')
    minus_candy = input_check_int_game()
    col_candy = col_candy - minus_candy
    print(f'Конфет осталось {col_candy}')
    if col_candy == 1:
        print(f'Проиграл игрок {second_player}!')
        break



# input_check_int()