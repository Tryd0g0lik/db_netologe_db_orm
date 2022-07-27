from peewee import *
# from db_orm.model.sql.sql_manager.sql_manager import BaseModel
from db_orm.crs.model.sql.sql_manager.sql_manager import BaseModel


class Shop(BaseModel):
  name = CharField(null = False)

  class Meta:
    db_orm = "Shop"
