from fastapi import FastAPI
from router import user_router
from models.db import Base, engine, get_db
from models.shemas_db import User
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
import crud

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(user_router)

