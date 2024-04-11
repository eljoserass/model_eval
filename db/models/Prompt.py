from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.models.Base import Base
from sqlalchemy.dialects.mysql import TEXT
from db.models.Session_Prompt import Session_Prompt


class Prompt(Base):
    name = Column(String(256), nullable=False)
    data = Column(TEXT, nullable=False)
    sessions = relationship("Session", secondary=Session_Prompt.__tablename__, back_populates="prompts")