import psycopg2
from psycopg2 import Error
import config

try:
    con = psycopg2.connect(host=config.host,
                           port=config.port,
                           database=config.database,
                           user=config.user,
                           password=config.password)
    print('Соединение открыто')
except (Exception, Error) as e:
    print('Ошибка подключения к БД:', e)
    exit()
