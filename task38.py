# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.

# r - только чтение файла
# a - дозапись в файл
# w - перезапись файла


def show_data():
    """the function shows the contents of the directory"""
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read()
    return book

def new_data():
    """the function adds a string to the directory"""
    with open('data.txt', 'a', encoding='utf-8') as file:
        file.write(input('Enter new string: '+ '\n') )
    

def find_data():
    """the function looks for information in the directory"""
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
        temp = input('Which info looking for? ')
        for i in book:
            if temp in i:
                print(i)


def delete_person(name):
    """Delete data"""
    persons = input()
    with open("data.txt", "w", encoding="utf8" ) as file:
        for person in persons:
            if name != person:
                file.write(person)

def change_person(new_name, old_name):
    """Change data"""
    persons = input()
    with open("data.txt", "w", encoding="utf8" ) as file:
        for person in persons:
            if  old_name != person:
                file.write(person)
            else:
                file.write(new_name + "\n")



while True:
    mode = input('Select directory operation mode' + '\n'
                  +'0-search, 1-read file, 2-add info into file, 3-delete, 4-change, 5-exit: ')
    if mode == '1':
        print(show_data())
    elif mode == '0':
        find_data()
    elif mode == '2':
        new_data()
    elif mode == '3':
        name = input('which info you want to delete: ')
        delete_person(name)
    elif mode == '4':
        old_name = input('which info do you want to change: ')
        new_name = input('enter new value: ')
        change_person(new_name,old_name)
    elif mode == '5':
        break
    else:
        print('No mode')
