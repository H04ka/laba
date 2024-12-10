from reg import *
from auth import *
import json
from keyboard_folder import keyboard

def start_menu():
    while True:
        start_input = input("Зарегистрироваться(R)/Войти в аккаунт(A)")
        if start_input is 'R':
            registration()
            break
        elif start_input is "A":
            authorization()
            break
        else:
            print("Некорректный ввод, повторите снова")
start_menu()