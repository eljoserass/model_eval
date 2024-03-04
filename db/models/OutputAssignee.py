from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from db.models.Base import Base


class OutputAssignee(Base):
    output_id = Column(Integer, ForeignKey("output.ID"))
    assignee_id = Column(Integer, ForeignKey("assignee.ID"))