from peewee import *
from datetime import *
import psycopg2
from db_orm.crs.model.sql.db import db

from db_orm.crs.model.shop.shop import Shop
from db_orm.crs.model.sale.sale import Sale
from db_orm.crs.model.book.book import Book
from db_orm.crs.model.stock.stock import Stock
from db_orm.crs.model.publisher.publisher import Publisher
#
# with PostgresqlDatabase('bd_orm', user = 'postgres', password = 'nlo7',
#                         host = 'localhost', port = 5432) as db:

class _CreateBasic():
  def __init__(self, table_name, name_publisher = None, title_book = None,
               id_publisher = None, id_book = None, id_shop = None, name_shop = None,
               stock_count = None, sale_count = None, price = None, date_sale = None, id_stock = None
               ):
    self.table_name = table_name
    self.title_book = title_book
    self.id_publisher = id_publisher
    self.name_publisher = name_publisher
    self.name_shop = name_shop
    self.id_book = id_book
    self.id_shop = id_shop
    self.stock_count = stock_count
    self.sale_count = sale_count
    self.price = price
    self.date_sale = date_sale
    self.id_stock = id_stock

class CreateDBRows(_CreateBasic):
  def __dataTable(self):
    # CreateDBRows(self).__init__(self):

    self.data_tables = [
      {'Stock': [self.id_book, self.id_shop, self.stock_count]},
      {'Shop': [self.name_shop]},
      {'Book': [self.title_book, self.id_publisher]},
      {'Publisher': [self.name_publisher]},
      {'Sale': [self.price, self.date_sale, self.id_stock, self.sale_count]}
    ]

    for i in range(len(self.data_tables)):


      for dictionary_key in self.data_tables[i].keys():

        if dictionary_key == self.table_name:
          return self.data_tables[i]

        else:
          pass


  def _get_db_insert(self):

    tuple_data_keys = list((CreateDBRows.__dataTable(self)).keys())[0]
    tuple_data_valumes = list((CreateDBRows.__dataTable(self)).values())[0]

    print(f"""t tuple_data_keys: { tuple_data_keys}""")
    print("tuple_data_valumes:", tuple_data_valumes)


    if tuple_data_keys == 'Book':
      title_book = tuple_data_valumes[0]
      id_publisher = tuple_data_valumes[1]

      try:
        Book().create(title = title_book,\
                      id_publisher_id = id_publisher)
      except (psycopg2.Error) as er:
        print(f"""Error_: {er}""")
        return

    elif tuple_data_keys == 'Shop':
      name_shop_ = tuple_data_valumes[0]
      Shop.create(name = str(name_shop_))

    elif tuple_data_keys == 'Publisher':
      name_publisher = tuple_data_valumes[0]
      Publisher.create(name = name_publisher)

    elif tuple_data_keys == 'Stock':
      id_book = tuple_data_valumes[0]
      id_shop = tuple_data_valumes[1]
      count_ = tuple_data_valumes[2]
      Stock.create(id_book_id = id_book, id_shop_id = id_shop, count = count_)

    elif tuple_data_keys == 'Sale':
      price_ = tuple_data_valumes[0]
      date_ = date.today()
      id_stock_ = (tuple_data_valumes[2])
      sale_count = tuple_data_valumes[3]
      Sale.create(price = price_, data_sale = date_,\
                  id_stock_id=id_stock_, count = sale_count)

