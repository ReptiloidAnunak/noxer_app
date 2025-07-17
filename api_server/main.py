

from flask import Flask, render_template
from logger import set_logger
from api_server.services.products.save_products import save_products_to_db
from data_base.data_base import Base, engine

from data_base import models  # Import models to ensure they are registered with SQLAlchemy
Base.metadata.create_all(engine)


logger = set_logger("SERVER")

save_products_to_db()

def create_app():
    app = Flask(__name__)
    logger.info("✅ Flask app created")
    
    @app.route('/')
    def home():
        return render_template('index.html')
    return app

if __name__ == '__main__':
    
    # app = create_app()
    # app.run(debug=True, host="0.0.0.0", port=5555)

    save_products_to_db()