from peewee import *
from ..sql.sql_manager.sql_manager import BaseModel
from ..publisher.publisher import Publisher

class Book(BaseModel):
  title = CharField(null=False)
  id_publisher = ForeignKeyField(Publisher, field='id', on_update = 'ON UPDATER')

  class Meta:
    table_name = 'Book'