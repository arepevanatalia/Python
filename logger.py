from data_create import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"Выберите вариант записи данных\n\n"
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 Вариант: \n"
    f"{name};{surname};{phone};{address}\n"
    f"Выберите вариант: "))

    while var != 1 and var != 2:
        print ("Неверный ввод")
        var = int(input ("Введите вариант "))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")


def print_data():
    print('Вывод Варианта 1: \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range (len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
        print(''.join(data_first_list))

    
    print('Вывод Варианта 2: \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f: 
        data_second = f.readlines()
        print(*data_second)


def update_data():
    file_name = input("Введите имя файла (data_first_variant.csv или data_second_variant.csv): ")
    field_to_update = int(input("Введите номер поля для обновления (0 - имя, 1 - фамилия, 2 - телефон, 3 - адрес): "))
    new_value = input("Введите новое значение: ")
    search_field = int(input("Введите номер поля для поиска (0 - имя, 1 - фамилия, 2 - телефон, 3 - адрес): "))
    search_value = input("Введите значение для поиска: ")
    lines = []
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(';')
            if parts[search_field] == search_value:
                parts[field_to_update] = new_value
            lines.append(';'.join(parts) + '\n')

    with open(file_name, 'w', encoding='utf-8') as f:
        f.writelines(lines)

def delete_data():
    file_name = input("Введите имя файла (data_first_variant.csv или data_second_variant.csv): ")
    search_field = int(input("Введите номер поля для поиска (0 - имя, 1 - фамилия, 2 - телефон, 3 - адрес): "))
    search_value = input("Введите значение для поиска: ")
    lines = []
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(';')
            if parts[search_field] != search_value:
                lines.append(';'.join(parts) + '\n')

    with open(file_name, 'w', encoding='utf-8') as f:
        f.writelines(lines)