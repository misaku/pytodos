from App.Model.BaseModel import *
from App.Model.Local import *
from App.Model.Pessoa import *
from peewee import *

class Tarefa(BaseModel):
    id = AutoField()
    nome = CharField()
    descricao = TextField()
    pessoa =  ForeignKeyField(Pessoa, backref='tarefas')
    contato =  ForeignKeyField(Pessoa, backref='tarefas')
    local = ForeignKeyField(Local, backref='tarefas')
    feita = BooleanField()