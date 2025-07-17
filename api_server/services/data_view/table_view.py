
from data_base.models import Product, Category
from data_base.data_base import SessionLocal
from sqlalchemy.orm import joinedload


def get_products_all():
    with SessionLocal() as session:
        return session.query(Product).options(joinedload(Product.categories)).all()


def get_сategories_all():
    with SessionLocal() as session:
        return session.query(Category).options(joinedload(Category.products)).all()




