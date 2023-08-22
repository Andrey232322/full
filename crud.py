from sqlalchemy.orm import Session

from models.model_db import User
from models import shemas_db

def get_user(id: int,db ):
    return db.query(User).filter(User.id == id).first()

def create_user(data:shemas_db.User,db):
    user = User(id = data.id,name = data.name,last_name = data.last_name, active = data.active,register_time = data.register_time)
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception as e:
        print(e)
    return user

def update(data:shemas_db.User,db:Session,id:int):
    shem_user = db.query(User).filter(User.id==id).first()
    shem_user.name = data.name

    db.add(shem_user)
    db.commit()
    db.refresh(shem_user)

    return shem_user
def delete_user(db:Session,id:int):
    user = db.query(User).filter(User.id ==id).delete()
    db.commit()
    return user

def show_user_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()