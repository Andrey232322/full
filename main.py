from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
import crud
from models.db import get_db, Base, engine
from models.shemas_db import User as model_user
from models.shemas_db import Item as model_item


app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get('/home{id}')
def show_user(id : int = None,db:Session = Depends(get_db)):
    user = crud.get_user(id,db)
    return user

@app.post('/home/user')
def create_user(data: model_user = None,db:Session = Depends(get_db)):
    user = crud.create_user(data,db)
    return user

@app.post('/home/item')
def create_item(data: model_item = None,db:Session = Depends(get_db)):
    return crud.create_item(data,db)

