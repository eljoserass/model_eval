import uuid
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from Base import Base


class EvalSession(Base):
    """
    need to store eval session to label output into different experiments
    """
    id = Column(Integer, primary_key=True)
    session_name  = Column(String, nullable=False)