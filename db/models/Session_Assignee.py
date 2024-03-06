import uuid
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from db.models.Base import Base
from sqlalchemy import UniqueConstraint


class Session_Assignee(Base):
    session_id = Column(Integer, ForeignKey("session.ID"))
    assignee_id = Column(Integer, ForeignKey("assignee.ID"))

    __table_args__ = (UniqueConstraint("session_id", "assignee_id"), )