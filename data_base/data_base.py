from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from settings import DATABASE_URL


engine = create_engine(DATABASE_URL)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)