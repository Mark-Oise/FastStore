from sqlalchemy import Integer, Column, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    brand = Column(String, index=True)
    color = Column(String, index=True)
    storage = Column(Integer, index=True)
    description = Column(String)
    image_url = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())