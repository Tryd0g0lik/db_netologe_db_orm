from peewee import *
from ..sql.sql_manager.sql_manager import BaseMooel


class Shop(BaseMooel):
  name = CharField(null = False)

  class Meta:
    db_orm = "Shop"
