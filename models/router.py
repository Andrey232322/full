from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from models import crud
from models.shemas_db import User
from models.db import get_db

user_router = APIRouter(prefix='/users',tags=['user'])

@user_router.get('/{id}')
def show_user(id : int = None,db:Session = Depends(get_db)):
    user = crud.get_user(id, db)
    return user
@user_router.get('/')
def show_users_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.show_user_all(db, skip=skip, limit=limit)
@user_router.post('/')
def create_user(data: User  = None, db:Session = Depends(get_db)):
    user = crud.create_user(data, db)
    return user

@user_router.delete('/')
def delete_user(id:int,db:Session = Depends(get_db)):
    return crud.delete_user(db, id)

@user_router.put('/')
def update_user(id:int, data:User= None, db:Session = Depends(get_db)):
    return crud.update(data, db, id)