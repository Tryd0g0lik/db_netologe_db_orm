# from model.sql.create_db.create_db import DataBase
from functions import checkTableInSQL
from crs.model.sql.db import db_postgres

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
      Create_db_table()
      continue

    elif responce == 'i':
      crate_date_row()

    elif responce == 's':
      # select_get_db() Функцию удалил - работаю с ошибкой.
      from crs.model.sql.sql_manager.sql_manager import BaseModel

      print(BaseModel)

    elif responce == 'ex':
      break
