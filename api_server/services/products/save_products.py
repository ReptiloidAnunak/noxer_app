
from concurrent.futures import ThreadPoolExecutor
from logger import set_logger
from settings import API_SOURCES
from data_base.data_base import SessionLocal
from api_server.services.products.functions import get_prods_lst_from_api, save_category_to_db, save_product_to_db
from api_server.services.data_view.table_view import get_products_all
logger = set_logger("SAVE_PRODUCTS")

def save_products_to_db() -> list:
    logger.info("Starting to save products to the database...")
    products_lst_res = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        source_futures = [executor.submit(get_prods_lst_from_api, source) for source in API_SOURCES]
        prods_lists = [future.result() for future in source_futures]

        logger.info(f"Fetched {len(prods_lists)} product lists from API sources.")

        for prods_lst in prods_lists:
            products_lst_res.extend(prods_lst)
    
        for prod in products_lst_res:
            bundle_id = prod.get("Product_ID")
            bundle_name = prod.get("Product_Name")
            on_main=prod.get("OnMain", False)
            reviews_video=prod.get("reviews_video", [])
            categories_dicts = prod.get("categories", [])

            futures_categories = [executor.submit(save_category_to_db, cat_data) for cat_data in categories_dicts]
            rel_cats_lst = [future.result() for future in futures_categories]

            variations = prod["parameters"]
            
            futures_products = [executor.submit(
                save_product_to_db,
                var,
                bundle_id,
                bundle_name,
                on_main,
                reviews_video
            )
            for var in variations
        ]
            
            with SessionLocal() as session:
                products = [future.result() for future in futures_products]
                rel_cats_in_session = [session.merge(cat) for cat in rel_cats_lst]
                for product in products:
                    product = session.merge(product)
                    product.categories.extend(rel_cats_in_session)
                    session.commit()
                    logger.debug(f"Product {product.id} saved with categories {[cat.id for cat in rel_cats_in_session]}")
    logger.info(f"Total products saved: {len(products_lst_res)}")
    vars_amount = len(get_products_all())
    logger.info(f"Total units saved: {vars_amount}")





        