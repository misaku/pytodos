from peewee import *
from conection import db

class BaseModel(Model):
    class Meta:
        database = db

        