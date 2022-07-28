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

      for i in range(len(self.data_tables)):
        for dictionary_key in self.data_tables[i].keys():
          print(f"""dictionary_key: {dictionary_key}""")
          if dictionary_key == self.table_name:
            print(f"""dictionary_key: {dictionary_key} ==
            self.table_name: {self.table_name} """)
            return (self.table_name, self.data_tables[i])
          else:
            print(f"""dictionary_key: {dictionary_key} ==
  self.table_name: {self.table_name} """)
            print(f"""I: {i}""")

    def get_variable(self):
      tuple_response_data = CreateDBRows.__dataTable(self)
      print(f"""tuple_response_data[0]: {tuple_response_data[0]}""")
      rd = tuple_response_data[0]
        # = tuple_response_data[1][tuple_response_data[0]]
      globals()[str(rd)] = tuple_response_data[1][tuple_response_data[0]]
      print(f"Book: {Book}")


    # def createRowData(self):
    #
    #   print(f"tuple_response_data: {tuple_response_data}")
    #
    #
    #   try:
    #     with db.atomic():
    #       tuple_response_data[1]
    #       return tuple_response_data[0].create()



