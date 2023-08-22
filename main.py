from fastapi import FastAPI
from router import user_router
from models.db import Base, engine



app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(user_router)