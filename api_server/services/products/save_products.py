
from concurrent.futures import ThreadPoolExecutor

from settings import API_SOURCES
from api_server.services.products.functions import get_prods_lst_from_api, save_category_to_db, save_product_to_db


def save_products_to_db() -> list:
    # This function would typically save products to a database.
    products_lst_res = []
    for source in API_SOURCES:
        prods_lst = get_prods_lst_from_api(source)
        products_lst_res.extend(prods_lst)
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        for prod in products_lst_res:
            bundle_id = prod.get("Product_ID")
            bundle_name = prod.get("Product_Name")
            on_main=prod.get("OnMain", False)
            reviews_video=prod.get("reviews_video", [])
            categories_dicts = prod.get("categories", [])
            
            for cat_data in categories_dicts:
                executor.submit(save_category_to_db(cat_data))

            variations = prod["parameters"]
            for var in variations:
                executor.submit(save_product_to_db(
                    product_data=var,
                    bundle_id=bundle_id,
                    bundle_name=bundle_name,
                    on_main=on_main,
                    reviews_video=reviews_video
                ))



        