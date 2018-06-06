from sqlalchemy.orm import mapper
from  sqlalchemy  import Table,MetaData,Column,Integer,String,ForeignKey

metadata=MetaData()

user=Table("user",metadata,
           Column('id',Integer,primary_key=True),
           Column('name',String(59)))
         
class User(object):
         def __init__(self,id,name):
                  self.id=id
                  self.name=name
mapper(User,user)


