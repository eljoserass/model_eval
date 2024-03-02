from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from Base import Base


class OutputAssignee(Base):
    id = Column(Integer, primary_key=True)
    output_id = Column(Integer, ForeignKey('output.ID'))
    assignee_id = Column(Integer, ForeignKey('assignee.ID'))