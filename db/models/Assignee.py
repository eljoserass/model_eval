from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.models.Base import Base
from db.models.OutputAssignee import OutputAssignee
OutputAssignee.__tablename__,

class Assignee(Base):
    name = Column(String(256), nullable=False)
    email = Column(String(256), nullable=False, unique=True)
    outputs = relationship("Output", secondary=OutputAssignee.__tablename__, back_populates="assigness")
    