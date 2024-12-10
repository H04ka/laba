from main_menu import *
from admin_menu import *
def authorization():
    print('\nДобро пожаловать в мир танков и пидпиваства')
    username_input = input('Введите логин:')
    password_input = input('Введите пароль:')
    for data_user in data["users"]:
        if username_input.lower() == data_user["username"].lower() and password_input.lower() == data_user["password"].lower():
            print(f'\nС повторным входом в рекламу балтики 9, {username_input}!')
            main_menu()
            break
        elif username_input.lower() == "admin_" and password_input == "admin_":
            print('Открыть панель админа')
            admin_menu()
            break
        else:
            pass
    else:
        print("Неверные данные, повторите заного")
        