from fastapi import APIRouter, HTTPException

from database import SessionLocal
from schemas import Product
import crud

products_router = APIRouter()


@products_router.get("/")
async def get_products():
    db = SessionLocal()
    return crud.get_products(db)


@products_router.get("/{product_id}")
async def get_product(product_id: int):
    db = SessionLocal()
    product = crud.get_product(db, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@products_router.post("/")
async def add_product(product: Product):
    db = SessionLocal()
    return crud.add_product(db, product)


@products_router.put("/{product_id}")
async def update_product(product_id: int, product: Product):
    db = SessionLocal()
    db_product = crud.get_product(db, product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return crud.update_product(db, db_product, product)


@products_router.delete("/{product_id}")
async def delete_product(product_id: int):
    db = SessionLocal()
    # throw exception if product_id does not exist
    product = crud.get_product(db, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return crud.delete_product(db, product_id)
