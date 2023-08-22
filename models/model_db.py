from sqlalchemy import Column,String,INTEGER,BOOLEAN
from models.db import Base

class User(Base):
    __tablename__ = 'User'

    id = Column(INTEGER,primary_key=True)
    name = Column(String)
    last_name = Column(String)
    active = Column(BOOLEAN)

class Item(Base):
    __tablename__ = 'Item'

    id = Column(INTEGER,primary_key=True)
    adres = Column(String)
    phone = Column(INTEGER)
    price = Column(INTEGER)
