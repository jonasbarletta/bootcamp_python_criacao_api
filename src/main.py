from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from src import models
from src import database
from typing import List, Union
from src.schema import Item, ItemBase, ItemCreate


app = FastAPI()

# Cria as tabelas no banco de dados, apenas se elas não existirem
models.Base.metadata.create_all(bind=database.engine)


# Home
@app.get("/")
def root():
    return {"message": "API ON"}

# Endpoint POST para criar um novo item
@app.post("/items/", response_model=Item)  
def create_item(item: ItemCreate, db: Session = Depends(database.get_db)):
    db_item = models.Item(**item.dict())  # Converte o objeto Pydantic em um modelo SQLAlchemy
    db.add(db_item)                       # Adiciona à sessão do banco
    db.commit()                           # Salva no banco de dados
    db.refresh(db_item)                   # Atualiza com dados gerados automaticamente (ex: id)
    return db_item                        # Retorna o item recém-criado

# Endpoint GET que retorna uma lista de itens
@app.get("/items/", response_model=List[Item])  
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    items = db.query(models.Item).offset(skip).limit(limit).all()  # Busca os itens com paginação
    return items  # Retorna a lista

# Endpoint GET que retorna um item específico chamado pelo id
@app.get("/items/{item_id}", response_model=Item)  
def read_item(item_id: int, db: Session = Depends(database.get_db)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()  # Busca pelo ID
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")  # Se não encontrar, retorna 404
    return db_item  # Retorna o item encontrado

# Endpoint PUT que atualiza um item específico chamado pelo id
@app.put("/items/{item_id}", response_model=Item)  
def update_item(item_id: int, item: ItemCreate, db: Session = Depends(database.get_db)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()  # Busca o item
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")  # 404 se não existir

    # Atualiza os atributos do item com os valores recebidos
    for key, value in item.dict().items():
        setattr(db_item, key, value)

    db.commit()           # Salva as alterações
    db.refresh(db_item)   # Atualiza o objeto com dados atualizados
    return db_item        # Retorna o item atualizado

# Endpoint DELETE que deleta um item específico chamado pelo id
@app.delete("/items/{item_id}", response_model=Item)  
def delete_item(item_id: int, db: Session = Depends(database.get_db)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()  # Busca o item
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")  # 404 se não existir

    db.delete(db_item)  # Marca para deletar
    db.commit()         # Confirma a exclusão no banco
    return db_item      # Retorna o item que foi deletado
