from peewee import *
from db_orm.crs.model.sql.sql_manager.sql_manager import BaseModel

from db_orm.crs.model.book.book import Book
from db_orm.crs.model.shop.shop import Shop


class Stock(BaseModel):
  id_book = ForeignKeyField(Book, field = 'id')
  id_shop = ForeignKeyField(Shop, field='id')
  count = IntegerField()

  class Meta:
    table_name = 'Stock'
