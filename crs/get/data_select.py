import peewee
# import psycopg2
from db_orm.crs.model.publisher.publish import Publisher

class filter():
  def __init__(self, name=None, id_=None):
    self.name = name
    self.id_ = id_

  def one_publisher(self):
    name_var = str(self.name).strip().strip(",.")

    id_var = self.id_
    f = None
    f_ = None

    if name_var != None and id_var == None:
      f = Publisher.select(Publisher.name, Publisher.id) \
        .where(Publisher.name.contains(f'''{name_var}'''))

    elif id_var != None and name_var == 'None':
      f_ = Publisher.select().where(Publisher.id == id_var)

      print(f_[0].id, f_[0].name)


    elif id_var != None and name_var != 'None':
      f = Publisher.select().where(Publisher.name == name_var)
      f_ = Publisher.select().where(Publisher.id == id_var)

      if f[0] == f_[0]:
        print(f[0].id, f[0].name)
      else:
        for v_var in [f, f_]:
          print(v_var[0].id, v_var[0].name)
      exit()



    else:
      f = Publisher.select().where(Publisher.name == name_var)
      exit()




