from sqlalchemy.orm import Session

from models import ProductDB
from schemas import Product


def get_products(db: Session):
    return db.query(ProductDB).all()


def get_product(db: Session, product_id: int):
    return db.query(ProductDB).filter(ProductDB.id == product_id).first()


def add_product(db: Session, product: Product):
    db_product = ProductDB(name=product.name, description=product.description, price=product.price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(db: Session, db_product: ProductDB, product: Product):
    # check if values exist before updating
    if product.name is not None:
        db_product.name = product.name
    if product.description is not None:
        db_product.description = product.description
    if product.price is not None:
        db_product.price = product.price
    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int):
    db_product = db.query(ProductDB).filter(ProductDB.id == product_id).first()
    if db_product is None:
        return None
    db.delete(db_product)
    db.commit()
    return db_product
