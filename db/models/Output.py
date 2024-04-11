import uuid
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from db.models.Base import Base
from sqlalchemy.orm import relationship
from db.models import Assignee_Output
from db.models.Assignee_Output import Assignee_Output
from sqlalchemy import UniqueConstraint
from sqlalchemy.dialects.mysql import MEDIUMTEXT



class Output(Base):
    """
    need to store ouputs to distribute them
    need to store its input to distribute it with the output
    need to store the model to back track who is responsable
    need to store the input and the model to check whether the input has been already runned in any case that 
        inputs want to be runned through models by batches
    need to store hash to distribute it to participants, wont distribute with model id as it could insert bias as from which model came from
    need to store session id to not mix input->output relation, if two output have the same input_id but different session is OK
        this will be used in any case a session stopped, that want to be runned by batches, and for stage 2 that we will test different prompt templates
    """
    model_id = Column(Integer, ForeignKey("model.ID"))
    session_id = Column(Integer, ForeignKey("session.ID"))
    input_id = Column(Integer, ForeignKey("input.ID"))
    data = Column(MEDIUMTEXT, nullable=False)
    
    model = relationship("Model", back_populates="outputs")
    session = relationship("Session", back_populates="outputs")
    input = relationship("Input", back_populates="outputs")
    assignees = relationship("Assignee", secondary=Assignee_Output.__tablename__, back_populates="outputs", overlaps="assignee_outputs,assignees,assignee")
    
    assignee_outputs = relationship("Assignee_Output", back_populates="output")
    
    
    
    __table_args__ = (UniqueConstraint("model_id", "session_id", "input_id"), )
    
    def __repr__(self):
        return f"Output: <model_id: {self.model_id}, session_id: {self.session_id}, input_id: {self.input_id}, data: {self.data}"
        