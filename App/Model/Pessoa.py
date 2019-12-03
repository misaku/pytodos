from App.Model.BaseModel import *
from peewee import *

class Pessoa(BaseModel):
    id = AutoField()
    nome = CharField()
    email = CharField()
    senha = TextField()