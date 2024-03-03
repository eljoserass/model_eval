from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_PATH = 'sqlite:///./beta.db'
engine = create_engine(DB_PATH, connect_args={"check_same_thread": False}, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()