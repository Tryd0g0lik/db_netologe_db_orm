from peewee import *
from db_orm.crs.model.sql.sql_manager.sql_manager import BaseModel

class Publisher(BaseModel):
  name = CharField(null=False)


  class Meta:
    table_name = 'Publisher'


