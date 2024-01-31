import os

def add_new_user(name: str, phone: str, filename: str):
    """
    Добавление нового пользователя.
    """
    with open(filename, 'a', encoding = 'UTF-8') as data:
        lines = read_all(filename)
        l = lines.count('\n')
        data.write(f"{l+1};{name};{phone}\n")
        return 'Запись добавлена'
        # return res if res != '' else 'Файл пустой'


def read_all(filename: str) -> str:
    """
    Возвращает все содержимое телефонной книги.
    """
    with open(filename, 'r', encoding = 'UTF-8') as data:
        res = data.read()
        return res if res != '' else 'Файл пустой'


def search_user(data: str, filename: str) -> str:
    """
    Поиск записи по критерию data.
    """
    with open(filename, 'r', encoding = 'UTF-8') as content:
        text = content.readlines()
        res = ([item for item in text if data.lower() in item.lower()])
    return (''.join(res)).replace(';', ' ') if res else 'Вхождений не найдено'



def file_exists(file: str):
    return (file in os.listdir())

INFO_STRING = """
Выберите ркжим работы:
1 - вывести все данные
2 - добавление нового пользователя
3 - поиск
"""

DATA_SOURCE = 'phones.txt'

if not file_exists(DATA_SOURCE):
    open(DATA_SOURCE, 'w', encoding = 'UTF-8')

while True:
    mode = int(input(INFO_STRING))
    if mode == 1:
        print(read_all(DATA_SOURCE))
        exit()
    elif mode == 2:
        name = input('Введите имя: ')
        phone = input('Введите номер телефона: ')
        print(add_new_user(name, phone, DATA_SOURCE))
        exit()
    elif mode == 3:
        search = input('Введите строку для поиска: ')
        print(search_user(search, DATA_SOURCE))
        exit()
