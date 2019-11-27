from BaseModel import *
from peewee import *

class Login(BaseModel):
    id = IdentityField()
    nome = CharField()
    email = CharField()
    senha = TextField()