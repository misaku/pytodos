from peewee import *
from App.Model.BaseModel import *

class Local(BaseModel):
    id = AutoField()
    nome = CharField()
    endereco = TextField()
