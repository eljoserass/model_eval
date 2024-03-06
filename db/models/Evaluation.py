from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from db.models.Base import Base
from sqlalchemy import Enum as SQLAlchemyEnum
from enum import Enum
from db.models.Session_Model import Session_Model

class Evaluation(Base):
    assignee_output_id = Column(Integer, ForeignKey("assignee_output.ID"))
    evaluation = Column(String(256)) #Need to change it
    
