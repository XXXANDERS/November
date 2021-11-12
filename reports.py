import requests
import os
from datetime import datetime
import config
URL_USERS = config.URL_USERS
URL_TODOS = config.URL_TODOS
DIR_PATH = os.path.dirname(__file__) + '/tasks'


def rename_file(filename: str) -> (bool, str):
    """Изменяет имя файла на имя с препиской old_ и добавлением datetime создания в конец названия. """
    try:
        with open(f"{DIR_PATH}/{filename}.txt", 'r') as f:
            f.readline()
            dt = f.readline()[-17:]  # в dt записиывается дата/время из файла
            dt_musk = f"{dt[6:10]}-{dt[3:5]}-{dt[:2]}T{dt[11:16]}"  # формат даты/времени в соответствии с требованиями
            new_filename = f"old_{filename}_{dt_musk}"
        os.rename(f"{DIR_PATH}/{filename}.txt", f"{DIR_PATH}/{new_filename}.txt")
        success = True
    except Exception as e:
        print('rename_file function exception :', e)
        new_filename = ''
        success = False

    return success, new_filename


def undo_rename(filename: str) -> None:
    """Возвращает прежнее имя файла. """
    try:
        os.rename(f"{DIR_PATH}/{filename}.txt", f"{DIR_PATH}/{filename[4:-17]}.txt")
    except Exception as e:
        print('undo_rename function exception:', e)


def write_file(filename: str, str_to_write: str, success_rename: bool = False, other_filename: str = '') -> None:
    """Записывает данные в файл, в случае неудачи, если для создания файла пришлось переименовать
    другой файл, возвращает старое название переименнованного файла.
    """
    try:
        with open(filename, 'w') as f:
            f.write(str_to_write)
            # print('Успешная запись для', filename)

    except Exception as e:
        print('write_file function exception:', e)
        if success_rename:
            undo_rename(other_filename)


def create_data(users_list, todos_list) -> None:
    """Создаёт отчёт по пользователям и вызывает функцию записи. """
    for user in users_list:
        try:
            # добавляем в список задания пользователя по его id.
            tasks = (x for x in todos_list if x.get('userId') == user['id'])
            str_to_write = f"Отчёт для {user['company'].get('name')}.\n"
            str_to_write += f"{user['name']} <{user.get('email','email отсутствует')}> "
            str_to_write += f"{datetime.today().strftime('%d.%m.%Y %H:%M')}\n"

            finished_tasks_str = ""
            unfinished_tasks_str = ""
            finished_tasks_count = 0
            tasks_count = 0

            for item in tasks:
                tasks_count += 1
                if item['completed']:
                    finished_tasks_str += f"{item['title'][:48]}\n"
                    finished_tasks_count += 1
                else:
                    unfinished_tasks_str += f"{item['title'][:48]}\n"

            str_to_write += f"Всего задач: {tasks_count}\n\n"
            str_to_write += f"Завершённые задачи ({finished_tasks_count}):\n"
            str_to_write += finished_tasks_str
            str_to_write += f"\nОставшиеся задачи ({tasks_count - finished_tasks_count}):\n"
            str_to_write += unfinished_tasks_str

            success_rename = False
            file_exist = os.path.exists(f"{DIR_PATH}/{user['username']}.txt")
            new_filename = ''
            if file_exist:
                success_rename, new_filename = rename_file(user['username'])

            write_file(filename=f"{DIR_PATH}/{user['username']}.txt",
                       str_to_write=str_to_write,
                       success_rename=success_rename,
                       other_filename=new_filename
                       )

        except Exception as e:
            print('Чтение данных не удалось:', e)


# Получаем данные с API
try:
    req_users = requests.get(URL_USERS)
    users_list = req_users.json()
    req_todos = requests.get(URL_TODOS)
    todos_list = req_todos.json()
    success_upload = True
except Exception as e:
    success_upload = False
    print('Загрузка данных не удалась:', e)

dir_exists = True

# создаём папку в случае необходимости
if not os.path.exists(DIR_PATH):
    try:
        os.mkdir(DIR_PATH)
    except Exception as e:
        dir_exists = False
        print('Создание папки не удалось: ', e)

if success_upload and dir_exists:
    create_data(users_list, todos_list)
