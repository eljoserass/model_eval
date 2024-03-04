from sqlalchemy.orm import as_declarative
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declared_attr
import uuid

@as_declarative()
class Base():
    __name__: str
    ID = Column(Integer, primary_key=True)
    uuid = Column(String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()