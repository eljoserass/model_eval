import uuid
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from db.models.Base import Base
from sqlalchemy import UniqueConstraint


class Assignee_Output(Base):
    assignee_id = Column(Integer, ForeignKey("assignee.ID"))
    output_id = Column(Integer, ForeignKey("output.ID"))

    __table_args__ = (UniqueConstraint("assignee_id", "output_id"), )