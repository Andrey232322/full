from sqlalchemy.orm import Session

from models.model_db import User, Item


def get_user(user_id: int,db ):
    return db.query(User).filter(User.id == user_id).first()

def create_user(data:list[User],db):
    db_user = User(id = data.id,name = data.name,last_name = data.last_name,active = data.active)
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except Exception as e:
        print(e)
    return db_user

def create_item(data:list[Item],db):
    db_user = Item(id = data.id,adres = data.adres,phone = data.phone,price = data.price)
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except Exception as e:
        print(e)
    return db_user