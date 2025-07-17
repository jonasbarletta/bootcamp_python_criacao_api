from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.sql import func
from src.database import Base

# Define o modelo ORM chamado 'Item'
# Este modelo será convertido em uma tabela chamada 'items' no banco de dados
class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key = True, index = True) # chave primária
    name = Column(String, nullable = False, index = True)
    price = Column(Float)
    is_offer = Column(String, nullable = True)
    created_at = Column(DateTime, default = func.now()) 
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


