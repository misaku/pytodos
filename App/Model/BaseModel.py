from peewee import *
from App.Config.conection import db

class BaseModel(Model):
    class Meta:
        database = db

        