from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    id:int
    name: str
    last_name: str
    active: bool
    register_time: datetime | None= None
