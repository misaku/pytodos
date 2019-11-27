from conection import db

from Local import *
from Login import *
from Pessoa import *
from Tarefa import *

db.create_tables([Local,Login,Pessoa,Tarefa])