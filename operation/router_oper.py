from fastapi import APIRouter,Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from models.model_db import User
from models.db import get_db

router_oper = APIRouter(prefix='/orm',tags=['orm'])


@router_oper.get('/')
def get_user_without_orm(oper: int, session: Session = Depends(get_db)):
    stmt = select(User).where(User.id == oper)
    res = session.scalar(stmt)
    return res