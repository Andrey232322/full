from fastapi import FastAPI
from router import user_router
from models.db import Base, engine
from models.db import get_db
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
import crud

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(user_router)

@app.get('/home/')
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.show_user_all(db, skip=skip, limit=limit)
