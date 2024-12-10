import json
from keyboard_folder import keyboard
import random

with open('user_data.json', 'r') as json_file:
    data = json.load(json_file)

print(data)
user = data["users"][0]
username =user["username"]
user_pass = user["password"]
print(username)
print(user_pass)


def main_menu():
    print(f'//ГЛАВНОЕ МЕНЮ')
    main = input("Включить игру(A)/ Выйти(R)")
    if main is "A":
        play()
    else:
        exit()


    #Здесь то чем будет пользоватся пользователь

#Старт менюшки
if __name__ == "__main__":
    print('\n Скрипт запущен в этом документе')
else:
    print('Скрипт импортирован')

def play():
    start_game = input("Хoтите сыграть? - Да(R)/ Нет(A)")
    if start_game is "R":
        print('Кубик')
        keyboard.wait('Enter')
        print(f'Вы выбросили: {random.randint(1,6)}')
    elif start_game is "A":
        print("Тогда кури бамбук")

def exit():
    ex = input("Вы уверены? Да(R)/ Нет(A)")
    if ex is "A":
        main_menu()
    elif ex is "R":
        print("ok")