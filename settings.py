import os
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent

LOGS_DIR = ROOT_DIR / "logs"

DB_DIR = ROOT_DIR / "data_base"


LOGS_DIR = ROOT_DIR / 'logs'
LOGS_MAIN = str(LOGS_DIR / 'main.logs')


API_SOURCES = ['https://bot-igor.ru/api/products?on_main=true',
               'https://bot-igor.ru/api/products?on_main=false']

os.makedirs(LOGS_DIR, exist_ok=True)
os.makedirs(DB_DIR, exist_ok=True)