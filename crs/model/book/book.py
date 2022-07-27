from peewee import *
from db_orm.crs.model.sql.sql_manager.sql_manager import BaseModel
from db_orm.crs.model.publisher.publisher import Publisher

class Book(BaseModel):
  title = CharField(null=False)
  id_publisher = ForeignKeyField(Publisher, field='id')

  class Meta:
    table_name = 'Book'