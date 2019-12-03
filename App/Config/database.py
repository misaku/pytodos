from App.Config.conection import db
from App.Model.Local import *
from App.Model.Pessoa import *
from App.Model.Tarefa import *

db.create_tables([Local,Pessoa,Tarefa])