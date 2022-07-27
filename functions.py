import psycopg2
import sys

# from model.sql.sql_manager.sql_manager import BaseModel
from db_orm.crs.model.stock.stock import Stock
from db_orm.crs.model.shop.shop import Shop
from db_orm.crs.model.book.book import Book
from db_orm.crs.model.publisher.publisher import Publisher
from db_orm.crs.model.sale.sale import Sale

# Check availabity the table of DB
def __referenceInModel():
  i = 0
  while True:
    if i == 3:
      return None

    print("""
    DB 'db_orm' can to have tables:
     - Book;
     - Publisher;
     - Sale;
     - Shop;
     - Stock 
     Insert only one the table name
    """)
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

