# from model.sql.create_db.create_db import DataBase
from functions import checkTableInSQL
from crs.model.sql.db import db_postgres
from db_orm.functions import select_get_db, crate_date_row, checkTableInSQL
from db_orm.functions import Create_db_table


while True:

  print("""Do you want:
   - create database      - 'db';
   - check presence table - 'pt';
   - create table         - 'ct';
   - exite or stop        - 'ex';
   
   - insert data          - 'i';
   - select data Publisher- 's'
   - """)
  responce = input(": ")
  responce = (responce).strip(" ").lower()
  responce_len = len(responce.split(" "))



  if responce_len == 1:
    if responce == 'db':
      DSN = """postgres://postgres:nlo7@localhost:5432/bd_orm"""
      continue

    elif responce == 'pt':
      checkTableInSQL()

      continue

    elif responce == 'ct':
      print("""You are created more one teble. It's: Publisher, Shop, Book,Stock, Sale""")
      Create_db_table()
      continue

    elif responce == 'i':
      crate_date_row()

    elif responce == 's':
      select_get_db()

    elif responce == 'ex':
      break
