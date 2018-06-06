import sqlalchemy as sqla
from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy.orm import sessionmaker,relationship

Base=declarative_base()
class Table(Base):
         __tablename__='sqla_t'
         id=sqla.Column(sqla.Integer,primary_key=True)
         name=sqla.Column(sqla.String(50))
         def __repr__(self):
                  return '<Table(id="%s",name="%s")>'%(self.id,self.name)


class Address(Base):
         __tablename__='address'
         id=sqla.Column(sqla.Integer,primary_key=True)
         email_adress=sqla.Column(sqla.String,nullable=False)
         table_id=sqla.Column(sqla.Integer,sqla.ForeignKey('table.id'))

         table=relationship("Table",back_populates='address')
         def __repr__(self):
                  return "<Address(email_address='%s')>"%self.email_address
engine=sqla.create_engine('mysql+mysqldb://root:love512105@localhost/one')
Session=sessionmaker(bind=engine)
session=Session()
