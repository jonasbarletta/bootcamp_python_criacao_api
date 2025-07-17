from pydantic import BaseModel, PositiveFloat, PositiveInt
from typing import Union
from datetime import datetime

 # Para validacao dos tipos de dados
class ItemBase(BaseModel): # contrato de dados, schema de dados, view da api
    name: str
    price: PositiveFloat
    is_offer: Union[bool, None] = None

    class Config:
        from_attributes = True # para comunicar com o ORM (sqlalchemy)

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: PositiveInt
    created_at: datetime
    updated_at: datetime

