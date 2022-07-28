import psycopg2
import sys
from datetime import *

# Model
from db_orm.crs.model.stock.stock import Stock
from db_orm.crs.model.shop.shop import Shop
from db_orm.crs.model.book.book import Book
from db_orm.crs.model.publisher.publisher import Publisher
from db_orm.crs.model.sale.sale import Sale

# CRUD
from crs.create_get.creating import *

def _returnNameTableDB():
  print("""
      DB 'db_orm' can to have tables:
       - Book;
       - Publisher;
       - Sale;
       - Shop;
       - Stock 
       Insert only one the table name
      """)

# Check availabity the table of DB
def __referenceInModel():
  i = 0
  while True:
    if i == 3:
      return None
    
    _returnNameTableDB()
    responce_var = input("Only one: ")
    responce_var = responce_var.strip()
    responce_len = len(responce_var.split(" "))

    if responce_len > 1:
      print("Repeat. ")


    else:
      return responce_var

    i += 1
# className_var = Publisher()


def checkTableInSQL():
  # print(f"222: ")
  responce_var = __referenceInModel()

  if responce_var == None:
    print("Fuuuu, loser!")
    exit()

  else:

    # print("0000")
    try:
      # className_var.SELECT(id = 0)
      responce_var.SELECT(id = 0)

    except (NameError, EnvironmentError, NameError,
            psycopg2.DataError, psycopg2.DatabaseError,
            psycopg2.ProgrammingError, psycopg2.Error, psycopg2.errors.UndefinedObject,
          AttributeError, psycopg2.errors.DuplicateDatabase,
            psycopg2.errors.UndefinedTable) as er:
      if psycopg2.errors.UndefinedTable or AttributeError:
        print("Can't fined the table")
        exit()
      else:
        print(f""""
        You are loser!
        
    Error_: {er},
    and
    {sys.exc_info()}
    """)
    exit()


# Create db-tables
def Create_db_table():
  list_tables = [Publisher, Shop, Book,Stock, Sale]

  for table_name in list_tables:
    table_name.create_table()
  print("Create tables!")

# create data row in TadaBase
def crate_date_row():
  print("""
  Enter a name data-table from the database 'bd-orm'  
  """)
  _returnNameTableDB()

  t_name = input("Single name: ")
  t_name = (t_name).strip().lower().capitalize()
  t_name_len = len(t_name.split(" "))

  if t_name_len == 1:
    if t_name == 'Book':
      print("title_book")
      title_book = input(': ' )
      title_book = (title_book).strip()
      print()

      print("id_publisher")
      id_publisher = input(": ")
      id_publisher = id_publisher.strip()
      cdbr = CreateDBRows(t_name, title_book = title_book, id_publisher = id_publisher)
      cdbr.get_variable()
      # cdbr.createRowData()
      # print("CreateDBRows))")

    elif t_name == 'Publisher':
        pass
    elif t_name == 'Sale':
        pass
    elif t_name == 'Shop':
        pass
    elif t_name == 'Stock':
        pass
    else:
      print("Repeat")
      return
    exit()
