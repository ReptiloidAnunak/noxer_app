import os
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent

DB_DIR = ROOT_DIR / 'data_base'

DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_NAME = os.getenv("DB_NAME", "noxer_db")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")


DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)



LOGS_DIR = ROOT_DIR / 'logs'
LOGS_MAIN = str(LOGS_DIR / 'main.logs')


API_SOURCES = ['https://bot-igor.ru/api/products?on_main=true',
               'https://bot-igor.ru/api/products?on_main=false']

os.makedirs(LOGS_DIR, exist_ok=True)
os.makedirs(DB_DIR, exist_ok=True)