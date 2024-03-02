from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from Base import Base


class Model(Base):
    """
    need to store models to know who is "responsable" for each output
    """
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    provider = Column(String, nullable=False)
    
    outputs = relationship('outputs', back_populates='model')