from sqlalchemy import Integer, Column, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    brand = Column(String, index=True)
    description = Column(String)
    image_url = Column(String)
    color = Column(String)
    storage = Column(String)
    price = Column(Float)
    quantity = Column(Integer)


