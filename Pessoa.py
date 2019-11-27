from BaseModel import *
from peewee import *

class Pessoa(BaseModel):
    id = IdentityField()
    nome = CharField()