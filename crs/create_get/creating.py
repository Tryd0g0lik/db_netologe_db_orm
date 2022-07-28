from peewee import *


with PostgresqlDatabase('bd_orm', user = 'postgres', password = 'nlo7',
                        host = 'localhost', port = 5432) as db:
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


      dict_name = self.table_name
      i = 0
      for dictionary_name in self.data_tables:
        print(dictionary_name[dict_name] == self.data_tables[dict_name])

        print(f"""I: {i}""")
        i += 1
      return

    def createRowData(self):
      CreateDBRows.__dataTable(self)
      print("CreateDBRows))")
      pass
      # try:
      #   with db.atomic():
      #     tables = self.table_name
          # return tables.create(data_tables)



