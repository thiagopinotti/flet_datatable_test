from peewee import *

database = SqliteDatabase('db/database.db')

class BaseModel(Model):
    class Meta:
        database = database

class Encomendas(BaseModel):
    id = AutoField()
    evento = CharField()
    cliente = CharField()
    data = CharField()
    cerimonial = CharField()
    local = CharField()
    horario = CharField()

database.create_tables([Encomendas])
