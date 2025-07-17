from flask import Flask, render_template, request
from logger import set_logger
from api_server.services.products.save_products import save_products_to_db
from data_base.data_base import Base, engine, SessionLocal
from data_base.models import Product, Category
import threading


Base.metadata.create_all(engine)


logger = set_logger("SERVER")


PAGE_SIZE = 10

def create_app():
    app = Flask(__name__)
    logger.info("✅ Flask app created")

    @app.route('/')
    def home():
        logger.info("🟢 Index page accessed")

        page = request.args.get('page', 1, type=int)

        with SessionLocal() as session:
            
            total_products = session.query(Product).count()
            total_categories = session.query(Category).count()

            
            products = (
                session.query(Product)
                .offset((page - 1) * PAGE_SIZE)
                .limit(PAGE_SIZE)
                .all()
            )

            
            categories = session.query(Category).all()

            
            for product in products:
                _ = product.categories

        
        total_pages = (total_products + PAGE_SIZE - 1) // PAGE_SIZE
        has_next = page < total_pages
        has_prev = page > 1

        
        return render_template(
            'index.html',
            products=products,
            categories=categories,
            page=page,
            has_next=has_next,
            has_prev=has_prev,
            total_pages=total_pages,
            total_products=total_products,
            total_categories=total_categories
        )
    return app


if __name__ == '__main__':
    threading.Thread(target=save_products_to_db, daemon=True).start()

    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5555)
