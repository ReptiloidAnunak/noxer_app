
from data_base.data_base import Base
from sqlalchemy import Table, Column, Integer, String, Float, Boolean, JSON, ForeignKey
from sqlalchemy.orm import relationship


association_table = Table(
    'product_category', Base.metadata,
    Column('product_id', Integer, ForeignKey('product.id', ondelete='CASCADE')),
    Column('category_id', Integer, ForeignKey('category.id', ondelete='CASCADE'))
)

class Category(Base):
    __tablename__ = 'category'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    sort_order = Column(Integer, nullable=True)
    image = Column(String, nullable=True)
    products = relationship('Product', secondary=association_table, 
                            back_populates='categories', passive_deletes=True)


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
    categories = relationship('Category', secondary=association_table, 
                              back_populates='products', passive_deletes=True)