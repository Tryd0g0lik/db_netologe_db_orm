from peewee import *
import sqlalchemy
import psycopg2
import sys


with PostgresqlDatabase('bd_orm', user = 'postgres', password = 'nlo7',
                        host = 'localhost', port = 5432) as db:

  class BaseModel(Model):
    id = PrimaryKeyField(unique=True, primary_key=True)

    class Meta:
      database = db
      order_by = id
