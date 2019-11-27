from peewee import *

db = PostgresqlDatabase('tododata', user='postgres', password='postgres',
                           host='localhost', port=5432)
db.connect()
