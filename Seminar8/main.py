# Создание телефонного спавочник
#
# 8.1[49]: Создать телефонный справочник с возможностью импорта и экспорта данных в формате csv. Доделать задание вебинара и реализовать Update, Delete
# Информация о человеке: Фамилия, Имя, Телефон, Описание
#
# Корректность и уникальность данных не обязательны.
#
# Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода.
# Выберите наиболее удобную структуру данных для хранения справочника.
#
# 2) CRUD: Create, Read, Update, Delete
#
# Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
# Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека. Берем первое совпадение по фамилии.
# Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
# Delete: Удаление записи из справочника. Выбор - как в Read.
# 3) экспорт данных в текстовый файл формата csv
#
# 4) импорт данных из текстового файла формата csv
#
# Используйте функции для реализации значимых действий в программе
#
# (*) Усложнение.
#
# Сделать тесты для функций
# Разделить на model-view-controller
# user = ["first_name", "second_name", "phone", "description"]
# phone_dict = {1: ["first_name", "second_name", "phone", "description"], 2: ["first_name", "second_name", "description"]}

from os.path import join, abspath, dirname

key_count = 0
phone_dict = {1:['Иванов', 'Иван', '+7(900)95686596', 'дуралей'],
              2:['Петров','Петр','+7(253)565685475','умник'],
              3:['Соколов','Илья','+7/655/656565848777','жадина']}
def input_users() -> list:
    user_input = []
    user_input.append(input("Введите имя пользователя: "))
    user_input.append(input("Введите фамилию пользователя: "))
    user_input.append(input("Введите телефон пользователя: "))
    user_input.append(input("Введите описание пользователя: "))

    return user_input


# print(input_users())

def create(phone_dict_loc: dict, user: list, idc: int) -> dict:
    idc += 1
    phone_dict_loc[idc] = user

    return phone_dict_loc, idc
# user1 = ["first_name", "second_name", "phone", "description"]
# user2 = ["first_name2", "second_name2", "phone2", "description2"]
# phone_dict, key_count = create(phone_dict, user1, key_count)
#phone_dict, key_count = create(phone_dict, user2, key_count)
#print(phone_dict)
def menu():
    key_count = 0
    phone_dict = {1:['Иванов', 'Иван', '+7(900)95686596', 'дуралей'],
              2:['Петров','Петр','+7(253)565685475','умник'],
              3:['Соколов','Илья','+7/655/656565848777','жадина']}
    print("Введите 0 ,если хотите выйти")
    print("Введите 1 ,если хотите добавить абонента")
    print("Введите 2 ,если хотите распечатать справочник")
    print("Введите 3 ,если хотите записать данные в файл")
    print("Введите 4 ,для поиска")

    while True:
        num = int(input("Выберите операцию: "))
        if num == 0:
            break
        if num == 1:
            user = input_users()
            phone_dict, key_count = create(phone_dict, user, key_count)
        if num == 2:
            print(phone_dict)
        if num == 3:
            file_name = input("Введите имя файла: ")
            export_phone_dict(phone_dict, file_name)
        if num == 4:
            search = input("Кого ищем?" + '\n')

def export_phone_dict(phone_dict: dict, file_name: str):
    MAIN_DIR = abspath(dirname(__file__))
    full_name = join(MAIN_DIR, file_name + '.txt')
    with open(full_name, mode='w', encoding='utf-8') as file:
        for key, val in phone_dict.items():
            file.write(f"{key},{val[0]},{val[1]},{val[2]},{val[3]}\n")

<<<<<<< HEAD

def export_phone_dict_to_csv(phone_dict: dict, file_name: str):
    MAIN_DIR = abspath(dirname(__file__))
    full_name = join(MAIN_DIR, file_name + '.csv')
    df = pd.DataFrame(phone_dict)
    df.to_csv(full_name, index=False, header=True)

def import_from_csv(file_name):
    MAIN_DIR = abspath(dirname(__file__))
    full_name = join(MAIN_DIR, file_name + '.csv')
    df = pd.read_csv(full_name, index_col=False)
    print(df)
def search_user(phone_dict: dict, searchstr: str) -> int:
=======
def search_user(phone_dict: dict, searchstr: str)-> int:
>>>>>>> parent of 98f4d9a (export_phone_dict_to_csv, update_users added)
    for key, val in phone_dict.items():
        if val[0].startswith(searchstr):
            return key

print(phone_dict)
print(search_user(phone_dict,'д'))
#menu()
# export_phone_dict(phone_dict, "phones")







<<<<<<< HEAD
#
# print(phone_dict)
# print(search_user(phone_dict,'д'))
#menu()
# export_phone_dict(phone_dict, "phones")
#export_phone_dict_to_csv(phone_dict, "phones11")
import_from_csv("phones11")
# print(update_user(phone_dict, 'Пе'))
# print(phone_dict)
=======
>>>>>>> parent of 98f4d9a (export_phone_dict_to_csv, update_users added)
