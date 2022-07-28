# from model.sql.create_db.create_db import DataBase
from functions import *
#
# # from model.sql.sql_manager.sql_manager import BaseModel
# from peewee import *

# print("""Do you want to create a new database?
# If yeas - 'y'
# If No -   'n'""")
# responce_new_db = input("'y' or 'n': ")
# responce_new_db = (responce_new_db).strip()
# responce_new_db_len = len(responce_new_db.split(" "))
# i = 0

# #
# while True:
#
#   if i == 3:
#     exit()
#
#   if responce_new_db == 'y' and responce_new_db_len == 1:
#     import model.sql.create_db.create_db
#
#   elif responce_new_db == 'n' and responce_new_db_len == 1:
#
#     break
#
#   else:
#     print("You are a loser! Repeat.")
#     exit()
#   i += 1

while True:

  print("""Do you want:
   - create database      - 'db';
   - check presence table - 'pt';
   - create table         - 'ct';
   - exite or stop        - 'ex';
   
   - insert data          - 'i';
   - """)
  responce = input(": ")
  responce = (responce).strip(" ").lower()
  responce_len = len(responce.split(" "))



  if responce_len == 1:
    if responce == 'db':
      DSN = """postgres://postgres:nlo7@localhost:5432/db_orm"""
      continue

    elif responce == 'pt':
      checkTableInSQL()

      continue

    elif responce == 'ct':
      Create_db_table()
      continue

    elif responce == 'i':
      crate_date_row()

    elif responce == 'ex':
      break
