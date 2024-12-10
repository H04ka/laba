from main_menu import*
from keyboard_folder import keyboard
import json

def registration():
    print("Регистрация")
    reg_name_input = input("Введите новый логин: ")
    reg_pass_input = input("Введите новый пароль: ")
    user["username"] = reg_name_input
    user["password"] = reg_pass_input
    data["users"].append(user)
    with open('user_data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Вы успешно зарегистрировались в танках, добро пожаловать в бухляндию {reg_name_input} для продолжения нажмите Enter и бахните пива")
    if keyboard.wait('Enter'):
        print('Enter нажат!')
        main_menu()
        