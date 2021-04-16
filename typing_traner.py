from time import *


# функция выбора режима

def select_mode():
    printable('''
Выберите режим:
1 - режим букв
2 - режим фраз
3 - режим тест скорости\n''', 0.05)
    global mode
    mode = input()
    return mode


# функция печатающего текста

def printable(text, speed=0.08, cursor=0):
    for char in text:
        sleep(speed)
        print(char, end='')
    if cursor == 1:
        for i in '| | ':
                sleep(0.5)
                print(i, end='')
                print('\x08', end='')

printable('Введите ваше имя: ')

user_name = input()

printable(f'\nПриветствую Вас, {user_name}!\n')

sleep(1)

select_mode()

if mode == '1':
    print('\nВыбран режим "Буквы"')
#    mode_spell()
elif mode == '2':
    print('\nВыбран режим "Фразы"')
#    mode_phrase()
elif mode == '3':
    print('\nВыбран режим "Тест скорости"')
#    mode_speed_test()
