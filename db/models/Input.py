from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from Base import Base


class Input(Base):
    """
    need to store input to backtrack if input has been alreaady been runned trhough model and produced response
    """
    id = Column(Integer, primary_key=True)
    input_data = Column(String, nullable=False)
    outputs = relationship('outputs', back_populates='model')