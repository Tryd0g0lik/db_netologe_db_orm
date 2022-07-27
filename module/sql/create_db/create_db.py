import psycopg2
import sys

# def DataBase(name_db, users):

try:
  conn = psycopg2.connect(
    database="postgres",
    user = "postgres",
    password = "nlo7",
    host = "127.0.0.1",
    port = "5432"
  )
  conn.autocommit = True
  curs = conn.cursor()

  curs.execute(f"""
    CREATE DATABASE bd_orm 
    WITH OWNER postgres
    ENCODING utf8;
  """)
except (NameError, EnvironmentError, NameError,
        psycopg2.DataError, psycopg2.DatabaseError,
        psycopg2.ProgrammingError, psycopg2.Error, psycopg2.errors.UndefinedObject,
        AttributeError, psycopg2.errors.DuplicateDatabase) as er:
  print(f"""ERRORE_: {er},
and
{sys.exc_info()}""")

finally:
  if psycopg2.errors.DuplicateDatabase:
    print("Created the DB")
  else:
    print("You are a loser")
conn.rollback()
curs.close()
exit()

