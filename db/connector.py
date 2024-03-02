from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_path = 'beta.db'
engine = create_engine(f'sqlite:///{db_path}', echo=True)

Session = sessionmaker(bind=engine)
session = Session()