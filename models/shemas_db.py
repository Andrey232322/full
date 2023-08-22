from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    last_name: str
    active: bool

class Item(BaseModel):
    id: int
    adres: str
    phone: int
    price: int
