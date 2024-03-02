from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from db.models.Base import Base


class Input(Base):
    """
    need to store input to backtrack if input has been alreaady been runned trhough model and produced response
    """
    data = Column(String, nullable=False, unique=True)
    outputs = relationship("Output", back_populates="input")