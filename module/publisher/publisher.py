from peewee import *

from ..sql.sql_manager.sql_manager import BaseModel

class Publisher(BaseModel):
  name = CharField(null=False)


  class Meta:
    table_name = 'Publisher'


