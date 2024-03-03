from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from db.models.Base import Base
from sqlalchemy import Enum as SQLAlchemyEnum
from enum import Enum

class Provider(Enum):
    POE = "POE"
    REPLICATE = "REPLICATE"
    OLLAMA = "OLLAMA"

class Model(Base):
    """
    need to store models to know who is "responsable" for each output
    """
    name = Column(String, nullable=False, unique=True)
    provider = Column(SQLAlchemyEnum(Provider), nullable=False)
    outputs = relationship("Output", back_populates="model")
