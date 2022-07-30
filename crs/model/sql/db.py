from peewee import PostgresqlDatabase


def db():
  return PostgresqlDatabase('bd_orm', user='postgres', password='nlo7',
                            host='localhost', port=5432)
