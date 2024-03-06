import uuid
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from db.models.Base import Base
from sqlalchemy import UniqueConstraint


class Session_Input(Base):
    session_id = Column(Integer, ForeignKey("session.ID"))
    input_id = Column(Integer, ForeignKey("input.ID"))

    __table_args__ = (UniqueConstraint("session_id", "input_id"), )