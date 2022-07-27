from peewee import *
from db_orm.module.sql.sql_manager.sql_manager import BaseModel

from db_orm.module.book.book import Book
from db_orm.module.shop.shop import Shop


class Stock(BaseModel):
  id_book = ForeignKeyField(Book, field = 'id', on_update='ON UPDATER')
  id_shop = ForeignKeyField(Shop, field='id', on_update = 'ON UPDATER')
  count = IntegerField()

  class Meta:
    table_name = 'Stock'
