from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
import crud
from models.db import get_db, Base, engine
from models.shemas_db import User



app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get('/home{id}')
def show_user(id : int = None,db:Session = Depends(get_db)):
    user = crud.get_user(id,db)
    return user

@app.post('/home/user')
def create_user(data: User  = None, db:Session = Depends(get_db)):
    user = crud.create_user(data,db)
    return user
@app.get('/user/all')
def show_user(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.show_user_all(db,skip=skip,limit=limit)

@app.delete('/user/')
def delete_user(id:int,db:Session = Depends(get_db)):
    return crud.delete_user(db,id)

@app.put('/user')
def update_user(id:int, data:User= None, db:Session = Depends(get_db)):
    return crud.update(data,db,id)