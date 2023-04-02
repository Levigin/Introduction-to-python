'''Задачи с семинара'''

import json


# Задание No1
# 📌 Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
# 📌 Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# 📌 Имена пишите с большой буквы.
# 📌 Каждую пару сохраняйте с новой строки.


def names_json(txt_file: str, json_file: str) -> None:
    with open(txt_file, 'r', encoding='utf-8') as f_txt, \
            open(json_file, 'w', encoding='utf-8') as f_json:
        all_data = {}
        while data := f_txt.readline():
            name, number = data[:-1].split()
            number = int(number) if number.find('.') == -1 else float(number)
            all_data[name.capitalize()] = number
        json.dump(all_data, f_json, ensure_ascii=False, indent=4)


# Задание No2
# 📌 Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа(от 1 до 7).
# 📌 После каждого ввода добавляйте новую информацию вJSON файл.
# 📌 Пользователи группируются по уровню доступа.
# 📌 Идентификатор пользователя выступает ключём для имени.
# 📌 Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# 📌 При перезапуске функции уже записанные в файл данные должны сохраняться.

def get_user_info(json_file: str) -> None:
    used_ids = set()
    levels = set(range(1, 8))
    users = {}

    with open(json_file, 'r', encoding='utf-8') as f:
        users = json.load(f)

    for _, val in users.items():
        for _, id_ in val.items():
            used_ids.add(id_)

    while True:
        user_name, user_id, user_level = input(
            'Введите через пробел: имя идентификатор "уровень доступа"> ').split()
        user_id = int(user_id)
        if user_name == '':
            break

        while user_id in used_ids:
            print("Пользователь с таким id уже существует")
            user_name, user_id, user_level = input(
                'Введите через пробел: имя идентификатор "уровень доступа"> ').split()
        else:
            used_ids.add(id_)

        user_level = int(user_level)
        while user_level not in levels:
            print(f"Уровень доступа {user_level} не существует")
            user_name, user_id, user_level = input(
                'Введите через пробел: имя идентификатор "уровень доступа"> ').split()

        users.setdefault(user_level, {})[user_name] = user_id
        print(users)
        with open(json_file, mode='w', encoding='utf-8') as f_json:
            json.dump(users, f_json, ensure_ascii=False)


if __name__ == '__main__':
    names_json('data_prod.txt', 'prod.json')
    get_user_info('users.json')
