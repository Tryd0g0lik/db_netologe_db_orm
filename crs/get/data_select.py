from db_orm.crs.model.sql.db import db_postgres
from db_orm.crs.model.publisher.publish import Publisher

for str_var in ['Center star', 'Kichkovskiy']:
  f = Publisher.select().where(Publisher.name == str_var)
  print(f[0].id, f[0].name)

db_postgres.commit()
db_postgres.close()




у