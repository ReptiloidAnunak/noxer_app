from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine


engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/noxer_db")

class Base(DeclarativeBase):
    pass

SessionLocal = sessionmaker(bind=engine)