import uuid
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from db.models.Base import Base
from db.models.Session_Prompt import Session_Prompt
from db.models.Session_Input import Session_Input
from db.models.Session_Model import Session_Model
from db.models.Session_Assignee import Session_Assignee
from sqlalchemy.ext.hybrid import hybrid_property
import random


class Session(Base):
    """
    need to store eval session to label output into different experiments
    """
    name = Column(String(256), nullable=False, unique=True)
    description = Column(String(256))
    
    inputs = relationship("Input", secondary=Session_Input.__tablename__, back_populates="sessions")
    outputs = relationship("Output", back_populates="session")
    prompts = relationship("Prompt", secondary=Session_Prompt.__tablename__, back_populates="sessions")
    models = relationship("Model", secondary=Session_Model.__tablename__, back_populates="sessions")
    assignees = relationship("Assignee", secondary=Session_Assignee.__tablename__, back_populates="sessions")
    
    @hybrid_property
    def outputs_shuffled(self):
        shuffled_list = list(self.outputs)
        random.shuffle(shuffled_list)
        return shuffled_list
    
    @hybrid_property
    def assignees_shuffled(self):
        shuffled_list = list(self.assignees)
        random.shuffle(shuffled_list)
        return shuffled_list
    