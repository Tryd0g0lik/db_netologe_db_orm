
# from peewee import PostgresqlDatabase
# from db_orm.crs.model.publisher.publisher import *
# from ..model.sql.db import db
# from crs.model.sql.db import db

from db_orm.crs.model.sql.db import db_postgres
from db_orm.crs.model.publisher.publisher import Publisher

Publisher.select()
# Publisher.name(['Spring'])



# try:
# conn = db.connect()
# curs = conn.cursor()
# name = 'Kichkovskiy'
# Publisher.get(Publisher.name == name.lower().strip())
# Publisher.select()
# curs.execute("SELECT Publisher;")
# curs.fetchall()

print("00000")
# except (NameError, TypeError, AttributeError) as er:
#
#   print(f"""er: {er},
#     and
#     {sys.exc_info()}""")
