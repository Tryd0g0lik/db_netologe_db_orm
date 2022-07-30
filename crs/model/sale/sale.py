from peewee import FloatField, DateField, ForeignKeyField, IntegerField
from db_orm.crs.model.sql.sql_manager.sql_manager import BaseModel
from db_orm.crs.model.stock.stock import Stock

class Sale(BaseModel):
  price = FloatField()
  data_sale = DateField()
  # id_stock = PrimaryKeyField(Stock, field='id', on_update = 'ON UPDATER')
  id_stock = ForeignKeyField(Stock, field='id')
  count = IntegerField()


  class Meta:
    table_name = 'Sale'
