from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class OutputAssignee(Base):
    id = Column(Integer, primary_key=True)
    ouput_id = Column(Integer, ForeignKey('output.id'))
    assignee_id = Column(Integer, ForeignKey('assignee.id'))