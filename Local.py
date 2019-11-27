from peewee import *
from BaseModel import *

class Local(BaseModel):
    id = IdentityField()
    nome = CharField()
    endereco = TextField()
