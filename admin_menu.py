from main_menu import*

def admin_menu():
    while True:
        print("Меню админа запущено")
        print("Чтобы узнать как забанить подпивана напишите !help")
        admin_input = input("Что вы хотите сделать: ")
        match admin_input:
            case '!delete':
                delete_user_input = input('Кого хотите удалить из пользователей? (Enter name): ')
                users = data.get('users', [])
                new_users = [user for user in users if user['username'] != delete_user_input]
                #обновляем данные и записываем обратно в файл
                data['users'] = new_users
                with open('user_data.json', 'w') as json_file:
                    json.dump(data, json_file, indent=4)
            
            case '!delete_all':
                delete_all_user_input = input('Ты серьёзно хочешь удалить всех подпивасов?')
                for data_user in data["users"]:
                    updated_data = {}
                    for key, value in data_user.items():
                        if key == delete_all_user_input:
                            updated_data.update({key : value})
                        else:
                            removed_value = value
                        print(f"пользователь {removed_value} был выкинут за выпитое пиво")
                    else:
                        print('Ошибка')
                with open('user_data.json', 'w') as json_file:
                    json.dump (updated_data, json_file, indetn=4)

            case '!help':
                print("Теперь вам доступны команды: !help, !delete, !delete_all, !database чтобы вернуться в меню нажмите "R"")
                print('Чтобы вернуться к регистрации напишите !unlogin')

            case '!exit':
                print("Закрытие программы...")
                break

            case '!unlogin':
                pass
            case "!database":
               with open('User_data.json', 'r') as user_data_file:
                user_data_file = json.load(user_data_file)
                print(user_data_file)
                