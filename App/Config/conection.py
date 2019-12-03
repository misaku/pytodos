from peewee import *

db = PostgresqlDatabase('my_app', user='postgres', password='postgres',
                           host='localhost', port=5432)
db.connect()
