from peewee import PostgresqlDatabase


# def db_postgres():
#   return PostgresqlDatabase('bd_orm', user='postgres', password='nlo7',
#                             host='localhost', port=5432)
db_postgres = PostgresqlDatabase('bd_orm', user='postgres', password='nlo7',
                            host='localhost', port=5432)