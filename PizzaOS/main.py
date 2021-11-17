from validators import UsersValidator
from managers import UsersDBManager
from connection import con

commands_dict = {
    'list': lambda range_id: UsersDBManager(con).list(range_id=range_id),
    'create': lambda request: UsersDBManager(con).create(request),
    'retrieve': lambda pk: UsersDBManager(con).retrieve(pk),
    'update': lambda request, pk: UsersDBManager(con).update(request, pk),
    'partial_update': lambda request, pk: UsersDBManager(con).partial_update(request, pk),
    'destroy': lambda pk: UsersDBManager(con).destroy(pk)
}
validators_dict = {
    'username': lambda username: UsersValidator.username_validate(username),
    'phone': lambda phone: UsersValidator.phone_validate(phone),
    'name': lambda name: UsersValidator.name_validate(name),
    'range_id': lambda range_id: UsersValidator.range_id_validate(range_id)
}


def request_handler(request, command, pk=None):
    for key in request.keys():
        request[key] = input(f'Введите {key}\n')
        while not validators_dict[key](request[key]):
            request[key] = input(f'Введите удовлетворяющее поле {key}\n')

    if pk:
        commands_dict[command](request, pk)
    else:
        commands_dict[command](request)


while True:
    command = input('Введите команду\n')
    request = {
        'username': None,
        'phone': None,
        'name': None,
    }

    if command == 'list':
        range_id = input('Введите диапазон id через запятую:  x0, x1\n')
        range_id = tuple(range_id.replace(' ', '').split(','))
        i = 0
        while i < 3 and not validators_dict['range_id'](range_id):
            range_id = input('Введите диапазон id правильно!\n')
            range_id = tuple(range_id.replace(' ', '').split(','))
            i += 1

        if i == 3:
            continue

        range_id = (int(range_id[0]), int(range_id[1]))
        commands_dict[command](range_id)
        continue

    if command == 'create':
        request_handler(request=request, command=command)

    if command == 'retrieve':
        pk = input('Введите id записи\n')
        if pk.isdigit():
            commands_dict[command](pk=int(pk))

    if command == 'update':
        pk = input('Введите id записи\n')
        if pk.isdigit():
            request_handler(request=request, command=command, pk=int(pk))

    if command == 'partial_update':
        pk = input('Введите id записи\n')
        if pk.isdigit():
            request_handler(request=request, command=command, pk=int(pk))

    if command == 'destroy':
        pk = input('Введите id записи\n')
        if pk.isdigit():
            commands_dict[command](pk=int(pk))

    if command == 'dns':
        print("Информация о сервере PostgreSQL")
        print(con.get_dsn_parameters(), "\n")

    if command == 'exit':
        break

    if command == 'help':
        print('Доступные комманды: list, create, retrieve, update, partial_update, destroy, dns, help')

    else:
        print('Команда введена не верно!')
        print('Для помощи наберите help')

con.close()
print('Соединение закрыто')
print('Конец сеанса')
