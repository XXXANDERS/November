import psycopg2
from psycopg2 import Error
# from psycopg2._psycopg import cursor
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import config
connection = False
try:
    # Подключение к существующей базе данных
    connection = psycopg2.connect(host=config.host,
                                  port=config.port,
                                  database=config.database,
                                  user=config.user,
                                  password=config.password)
    # connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()
    # print("Информация о сервере PostgreSQL")
    # print(connection.get_dsn_parameters(), "\n")

    with open('create_users_table.sql', 'r') as f:
        cursor.execute(f.read())

    # cursor.execute(sql_create_database)
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)

finally:

    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
