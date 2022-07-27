from peewee import *
from ..sql.sql_manager.sql_manager import BaseModel
from ..stock.stock import Stock

class Sale(BaseModel):
  price = FloatField()
  data_sale = DateField()
  id_stock = PrimaryKeyField(Stock, field='id', on_update = 'ON UPDATER')
  count = IntegerField()

  class Meta:
    table_name = 'Sale'
