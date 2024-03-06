from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.settings import settings
from typing import Generator


SQLALCHEMY_DATABASE_URL = settings.DB_URL.unicode_string()

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#session = SessionLocal()


from contextlib import contextmanager


@contextmanager
def get_session() -> Generator:
    try:
        db = SessionLocal()
        yield db
    except Exception as e:
        print(f"Rolling Back [{e}]")
        db.rollback()
    finally:
        print("Closing Session")
        db.close()