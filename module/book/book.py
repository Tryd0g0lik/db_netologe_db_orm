from peewee import *
from db_orm.module.sql.sql_manager.sql_manager import BaseModel
from db_orm.module.publisher.publisher import Publisher

class Book(BaseModel):
  title = CharField(null=False)
  id_publisher = ForeignKeyField(Publisher, field='id', on_update = 'ON UPDATER')

  class Meta:
    table_name = 'Book'