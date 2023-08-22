from datetime import datetime

from sqlalchemy import Column,String,INTEGER,BOOLEAN,TIMESTAMP
from models.db import Base

class User(Base):
    __tablename__ = 'User'

    id = Column(INTEGER,primary_key=True)
    name = Column(String)
    last_name = Column(String)
    active = Column(BOOLEAN)
    register_time = Column(TIMESTAMP(timezone=True),nullable=False,)
