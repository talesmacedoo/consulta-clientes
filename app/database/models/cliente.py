from peewee import Model, CharField, DateTimeField
from database.database import db
import datetime

class Cliente(Model):
    nome = CharField()
    cpf = CharField()
    celular1 = CharField()
    celular2 = CharField()
    data_de_nascimento = CharField()
    data_atualizacao = CharField()

    class Meta:
        database = db
