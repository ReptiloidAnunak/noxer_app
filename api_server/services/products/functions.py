import requests
from sqlalchemy.exc import IntegrityError

from data_base.models import Product, Category
from data_base.data_base import SessionLocal







def get_api_dict(source: str) -> dict:
        response = requests.get(source)
        return response.json()


def get_prods_lst_from_api(source: str) -> list:
    json_data = get_api_dict(source)
    products = json_data.get("products", [])
    return products


def save_category_to_db(category_data: dict) -> Category:
    category = Category(
    id=category_data.get("Category_ID"),
    name=category_data.get("Category_Name"),
    sort_order=category_data.get("sort_order"),
    image=category_data.get("Category_Image")
    )
    with SessionLocal() as session:
        session.add(category)
        try:
            session.commit()
        except IntegrityError:
            session.rollback()
            print(f"Category with ID {category.id} already exists in the database.")

    return category


def save_product_to_db(product_data: dict,
                       bundle_id: int,
                       bundle_name: str,
                       on_main: bool,
                       reviews_video: list
                       ) -> Product:
    product = Product(
                id=product_data.get("Parameter_ID"),
                bundle_id = bundle_id,
                bundle_name=bundle_name,
                name=product_data.get("parameter_string"),
                price=product_data["price"],
                on_main=on_main,
                image=product_data.get("extra_field_image"),
                reviews_video=reviews_video
            )
    with SessionLocal() as session:
        session.add(product)
        try:
            session.commit()
        except IntegrityError:
            session.rollback()
            print(f"Product with ID {product.id} already exists in the database.")
    return product