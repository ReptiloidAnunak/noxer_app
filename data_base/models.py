
from data_base.data_base import Base, engine
from sqlalchemy import Column, Integer, String, Float, Boolean, JSON



class Product(Base):
    __tablename__ = 'product'
    
    id = Column(Integer, primary_key=True)
    bundle_id = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    bundle_name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    on_main = Column(Boolean, default=False)
    image = Column(String, nullable=True)
    reviews_video = Column(JSON, nullable=True)
