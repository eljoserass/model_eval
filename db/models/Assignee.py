from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Assingnee(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    outputs = relationship('outputs', back_populates='model')
    