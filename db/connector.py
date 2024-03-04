from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.settings import settings

SQLALCHEMY_DATABASE_URL = settings.DB_URL.unicode_string()

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()