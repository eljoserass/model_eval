from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from Base import Base


class Assingnee(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    outputs = relationship('outputs', back_populates='model')
    