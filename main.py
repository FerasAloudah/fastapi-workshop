from fastapi import FastAPI

from database import Base, engine
from router import products_router

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(products_router, prefix="/products", tags=["products"])


@app.get("/")
async def root():
    return {'message': "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
