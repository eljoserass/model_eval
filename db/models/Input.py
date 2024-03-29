from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from db.models.Base import Base
from sqlalchemy import Enum as SQLAlchemyEnum
from enum import Enum
from sqlalchemy.dialects.mysql import TEXT
from db.models.Session_Input import Session_Input


class Label(Enum):
    INFORMATION = "INFORMATION"
    ADVICE = "ADVICE"
    EMERGENCY = "EMERGENCY"
    JAILBREAK = "JAILBREAK"

class Input(Base):
    """
    need to store input to backtrack if input has been alreaady been runned trhough model and produced response
    """
    data = Column(String(500), nullable=False, unique=True)
    label = Column(SQLAlchemyEnum(Label), nullable=False)
    
    sessions = relationship("Session", secondary=Session_Input.__tablename__, back_populates="inputs")
    outputs = relationship("Output", back_populates="input")