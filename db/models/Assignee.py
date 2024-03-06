from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.models.Base import Base
from db.models.Assignee_Output import Assignee_Output
from db.models.Session_Assignee import Session_Assignee

class Assignee(Base):
    name = Column(String(256), nullable=False)
    email = Column(String(256), nullable=False, unique=True)
    outputs = relationship("Output", secondary=Assignee_Output.__tablename__, back_populates="assignees")
    sessions = relationship("Session", secondary=Session_Assignee.__tablename__, back_populates="assignees")