from sqlalchemy import Column,String,INTEGER,BOOLEAN
from models.db import Base

class User(Base):
    __tablename__ = 'User'

    id = Column(INTEGER,primary_key=True)
    name = Column(String)


