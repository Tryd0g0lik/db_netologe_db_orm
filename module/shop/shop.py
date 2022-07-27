from peewee import *
# from db_orm.module.sql.sql_manager.sql_manager import BaseModel
from db_orm.module.sql.sql_manager.sql_manager import BaseModel


class Shop(BaseModel):
  name = CharField(null = False)

  class Meta:
    db_orm = "Shop"
