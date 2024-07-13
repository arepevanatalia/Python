from logger import input_data, print_data, update_data, delete_data


def interface():
    print ("Вас приветствует бот-справочник! \n 1 - ввод данных, \n 2 - вывод данных, \n 3 - изменение данных, \n 4 - удаление данных, \n 5 - выход")
    command = int(input ("Введите номер "))

    while command != 1 and command != 2 and command != 3 and command != 4 and command != 5:
        print ("Неверный ввод")
        command = int(input("Введите номер "))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        update_data()
        print("Данные обновлены!")
    elif command == 4:
        delete_data()
        print("Данные удалены!")
    elif command == 5:
        return
    else:
        print("Неверный выбор.")
    