# from datetime import *
# import psycopg2

import sys
import re

from datetime import date
from  db_orm.crs.get.data_select import filter
# Model
from db_orm.crs.model.stock.stock import Stock
from db_orm.crs.model.shop.shop import Shop
from db_orm.crs.model.book.book import Book
from db_orm.crs.model.publisher.publish import Publisher
from db_orm.crs.model.sale.sale import Sale


# CRUD
from crs.create_get.creating import *

def _returnNameTableDB():
  print("""
      DB 'db_orm' can to have tables:
       - Shop;
       - Publisher;
       - Book;       
       - Stock 
       - Sale;
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


def checkTableInSQL():
  responce_var = __referenceInModel()

  if responce_var == None:
    print("Fuuuu, loser!")
    exit()

  else:

    try:
      responce_var.SELECT(id = 0)

    except (NameError, EnvironmentError, NameError,
            psycopg2.DataError, psycopg2.DatabaseError,
            psycopg2.ProgrammingError, psycopg2.Error, psycopg2.errors.UndefinedObject,
          AttributeError, psycopg2.errors.DuplicateDatabase,
            psycopg2.errors.UndefinedTable) as er:
      if psycopg2.errors.UndefinedTable or AttributeError:
        print("Sorry. This's function the closed")
        # print("Can't fined the table")
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
  while True:

    print("""
    Enter the name data-table from the database 'bd-orm' OR 
    enter the symbols 'ex' im order to be exit.  
    """)
    _returnNameTableDB()

    t_name = input("Single name: ")
    t_name = (t_name).strip().lower().capitalize()
    t_name_len = len(t_name.split(" "))

    if t_name == 'Ex':

      return

    elif t_name_len == 1:
      if t_name == 'Book':
        print("Title_book")
        title_book = input(': ' )
        title_book = (title_book).strip()
        print()

        print("id_publisher")
        id_publisher = input(": ")
        id_publisher = id_publisher.strip()
        cdbr = CreateDBRows(t_name, title_book = title_book, id_publisher = id_publisher)
        cdbr._get_db_insert()
        continue

      elif t_name == 'Publisher':


        print("Name")
        name_publisher = input(': ')
        name_publisher = (name_publisher).strip()
        print()

        cdbr = CreateDBRows(t_name, name_publisher=name_publisher)
        cdbr._get_db_insert()
        continue

      elif t_name == 'Sale':
        y = re.compile(r"[0-9]{4}", flags=0)
        m = re.compile("^[0-9]{1,}")
        d = re.compile(r"[0-9]{1,2}", flags=0)

        print("price")
        price = input(': ')
        price = float((price).strip())
        print()

        print("id_stock")
        id_stock = input(': ')

        if m.findall(id_stock):
          id_stock = int((id_stock).strip())
        else:
          print("Error into the inputted ID of Stock")

        print()
        date_sale = date.today()
        print("sale_count")
        sale_count = input(': ')
        if m.findall(sale_count):
          sale_count = int((sale_count).strip())
        else:
          print("Error into the inputted Count of Sale")
        print()

        cdbr = CreateDBRows(t_name, price=price, date_sale=date_sale,\
                            id_stock=id_stock, sale_count=sale_count)
        cdbr._get_db_insert()
        continue


      elif t_name == 'Shop':
        print("Name the the shop")
        name_shop = input(': ')
        name_shop = (name_shop).strip()
        print()

        cdbr = CreateDBRows(t_name, name_shop=name_shop)
        cdbr._get_db_insert()
        continue

      elif t_name == 'Stock':
        print("id-book from a Book db")
        id_book = input(': ')
        id_book = int((id_book).strip())
        print()

        print("id-shop from Shop db")
        id_shop = input(': ')
        id_shop = int((id_shop).strip())
        print()

        print("stock_count")
        stock_count = input(': ')
        stock_count = int((stock_count).strip())
        print()

        cdbr = CreateDBRows(t_name, id_book=id_book, id_shop=id_shop, stock_count=stock_count)
        cdbr._get_db_insert()
        continue

      else:
        print("Repeat")
        return

  exit()

# Select data from the table
def select_get_db():
  print("""==Get data  of Publishers==""")
  print("""Insert Id or publisher's name only an one publisher""")

  name_publisher = '%s, %s' % (input('Name: '), input('Id: '))
  name_publisher = (name_publisher).strip().split(", ")
  #
  name_var = re.compile(r"^[??-????-??A-Za-z]{1,}", re.I)
  id_var = re.compile(r"^[0-9]{1,}")
  #
  print(('len:_ ', len(name_publisher)))




  if len(name_publisher) > 1:
    if name_var.findall(str(name_publisher[0]).strip()):
        name = ((str(name_publisher[0]).strip().split(" "))[0]).strip("- ,")
    else:
      name = None

    if  (name_publisher[1]).strip() != None:
        id_ = int((name_publisher[1]).strip())
        print('id_: ', id_)
    else:
      id_ = None
    if name == None and id_ == None:

      print("You are loo-ser!")
      print(name, id_)
      exit()

    else:

      fltr = filter(name, id_)
      fltr.one_publisher()

  elif len(name_publisher) == 1:
    if name_var.findall((name_publisher[0]).strip()):
      name = str(name_publisher[0])

      fltr = filter(name)
      fltr.one_publisher()

    else:
      name = None

    if id_var.findall((name_publisher[0]).strip()):
      id_ = int((name_publisher[0]).strip())

      fltr = filter(id_)
      fltr.one_publisher()

    else:
      id_ = None

    if name == None and id_ == None:

      print("You are loo-ser!")
      print(name, id_)
      exit()




