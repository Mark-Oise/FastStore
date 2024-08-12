from pydantic import BaseModel
from typing import Optional


class ProductBase(BaseModel):
    name: str
    brand: str
    color: str
    storage: str
    description: Optional[str] = None
    image_url: Optional[str] = None
    price: float
    quantity: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True
