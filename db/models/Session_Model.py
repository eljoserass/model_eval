import uuid
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from db.models.Base import Base
from sqlalchemy import UniqueConstraint

class Session_Model(Base):
    session_id = Column(Integer, ForeignKey("session.ID"))
    model_id = Column(Integer, ForeignKey("model.ID"))

    __table_args__ = (UniqueConstraint("session_id", "model_id"), )
