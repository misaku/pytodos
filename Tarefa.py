from BaseModel import *
from Local import *
from Pessoa import *
from peewee import *

class Tarefa(BaseModel):
    id = IdentityField()
    nome = CharField()
    descricao = TextField()
    pessoa =  ForeignKeyField(Pessoa, backref='tarefas')
    contato =  ForeignKeyField(Pessoa, backref='tarefas')
    local = ForeignKeyField(Local, backref='tarefas')
    feita = BooleanField()