import os
from tkinter import *
from tkinter import filedialog

"""
DEFINES
"""
def add_new_user(name: str, phone: str, filename: str):
    """
    Добавление нового пользователя.
    """
    with open(filename, 'a', encoding = 'UTF-8') as data:
        lines = read_all(filename)
        print(lines)
        l = 0 if lines == False else lines.count('\n')
        data.write(f"{l+1};{name};{phone}\n")
        return 'Запись добавлена'
        # return res if res != '' else 'Файл пустой'


def read_all(filename: str) -> str:
    """
    Возвращает все содержимое телефонной книги.
    """
    with open(filename, 'r', encoding = 'UTF-8') as data:
        res = data.read()
        return res.replace(';', ' ') if res != '' else False


def search_user(data: str, filename: str) -> str:
    """
    Поиск записи по критерию data.
    """
    with open(filename, 'r', encoding = 'UTF-8') as content:
        text = content.readlines()
        res = ([item for item in text if data.lower() in item.lower()])
    return (''.join(res)).replace(';', ' ') if res else False


def get_lines(data: str, filename: str) -> str:
    """
    Поиск строк.
    """
    lines = data.split()
    content = read_all(filename)
    if content == False:
        return content
    res = list(filter(lambda el: el.split()[0] in lines, content.split('\n')))
    return res

def save_data(data: str, externalfile: str) -> str:
    """
    Передача записей из localfile в externalfile.
    """
    with open(externalfile, 'a+', encoding = 'UTF-8') as filedata:
        for item in data:
            add_new_user(item.split()[1], item.split()[2], externalfile)


def file_exists(file: str):
    return (os.path.basename(file) in os.listdir(os.path.dirname(file)))


"""
MAIN START POINT
"""

INFO_STRING = """
Выберите ркжим работы:
1 - вывести все данные
2 - добавление нового пользователя
3 - поиск
4 - экспорт записей
5 - выход
"""
CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
DATA_DIRECTORY = os.path.join(CURRENT_DIRECTORY, 'data')

DATA_SOURCE = os.path.join(DATA_DIRECTORY, 'phones.txt')

if not file_exists(DATA_SOURCE):
    print(f'File {DATA_SOURCE} not found. Creating...')
    f = open(DATA_SOURCE, 'w', encoding = 'UTF-8')
    f.close()


root = Tk()
root.withdraw()

while True:
    mode = int(input(INFO_STRING))
    if mode == 1:
        res = read_all(DATA_SOURCE)
        print('Файл пустой' if res == False else res)
    elif mode == 2:
        name = input('Введите имя: ')
        phone = input('Введите номер телефона: ')
        print(add_new_user(name, phone, DATA_SOURCE))
    elif mode == 3:
        search = input('Введите строку для поиска: ')
        if(search != ''):
            res = search_user(search, DATA_SOURCE)
            print('Вхождений не найдено' if res == False else res)
        else:
            print('Строка для поиска не должна быть пустой')
    elif mode == 4:
        search = get_lines(input('Введите строки для экспорта: '), DATA_SOURCE)
        if search == False:
            print(f'Данные не найдены в файле {DATA_SOURCE}')
        else:
            print(search)
            destfile = filedialog.asksaveasfilename(title='Выбор целевого файла', initialdir=os.path.join(CURRENT_DIRECTORY, 'data'), defaultextension="txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")], confirmoverwrite = False)
            if destfile != '':
                save_data(search, destfile)

    elif mode == 5:
        exit()


# 1;qqq;123
# 2;qwer;1234
# 3;vvv;515151