

from sqlalchemy.exc import IntegrityError
from settings import API_SOURCES
from data_base.models import Product
from data_base.data_base import SessionLocal
from api_server.services.products.functions import get_prods_lst_from_api



def save_products_to_db() -> list:
    # This function would typically save products to a database.
    products_lst_res = []
    for source in API_SOURCES:
        prods_lst = get_prods_lst_from_api(source)
        products_lst_res.extend(prods_lst)
    for prod in products_lst_res:
        bundle_id = prod.get("Product_ID")
        bundle_name = prod.get("Product_Name")
        on_main=prod.get("OnMain", False)
        reviews_video=prod.get("reviews_video", [])


        variations = prod["parameters"]

        for var in variations:

            product = Product(
                id=var.get("Parameter_ID"),
                bundle_id = bundle_id,
                bundle_name=bundle_name,
                name=var.get("parameter_string"),
                price=var["price"],
                on_main=on_main,
                image=var.get("extra_field_image"),
                reviews_video=reviews_video
            )

        print(product)
        with SessionLocal() as session:
            session.add(product)
            try:
                session.commit()
            except IntegrityError:
                session.rollback()
                print(f"Product with ID {product.id} already exists in the database.")



        