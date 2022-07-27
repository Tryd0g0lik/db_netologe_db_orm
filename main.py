# from module.sql.create_db.create_db import DataBase
from functions import checkTableInSQL

# from module.sql.sql_manager.sql_manager import BaseModel
from peewee import *
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
#     import module.sql.create_db.create_db
#
#   elif responce_new_db == 'n' and responce_new_db_len == 1:
#
#     break
#
#   else:
#     print("You are a loser! Repeat.")
#     exit()
#   i += 1

print("""Do you want:
 - check presence table - 'pt'
 - create table - 'ct';
 
 - """)
responce = input(": ")
responce = (responce).strip(" ").lower()
responce_len = len(responce.split(" "))

if responce_len == 1:
  if responce == 'ct':
    DSN = """postgres://postgres:nlo7@localhost:5432/db_orm"""
    exit()

  elif responce == 'pt':
    checkTableInSQL()
    exit()
