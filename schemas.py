from pydantic import BaseModel


class Product(BaseModel):
    id: int | None
    name: str | None
    description: str | None
    price: int | None

    class Config:
        orm_mode = True
