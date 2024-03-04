import uuid
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from db.models.Base import Base


class Session(Base):
    """
    need to store eval session to label output into different experiments
    """
    name  = Column(String(256), nullable=False, unique=True)
    outputs = relationship("Output", back_populates="session")