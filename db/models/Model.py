from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from db.models.Base import Base
from sqlalchemy import Enum as SQLAlchemyEnum
from enum import Enum
from db.models.Session_Model import Session_Model

class Provider(Enum):
    POE = "POE"
    REPLICATE = "REPLICATE"
    OLLAMA = "OLLAMA"

class Model(Base):
    """
    need to store models to know who is "responsable" for each output
    """
    name = Column(String(256), nullable=False, unique=True)
    provider = Column(SQLAlchemyEnum(Provider), nullable=False)
    
    sessions = relationship("Session", secondary=Session_Model.__tablename__, back_populates="models")
    outputs = relationship("Output", back_populates="model")
