from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/teste")
async def root():
    return {"message": "Hello Teste"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}