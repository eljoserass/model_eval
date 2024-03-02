import uuid
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from Base import Base


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
    id = Column(Integer, primary_key=True)
    model_id = Column(Integer, ForeignKey('model.ID'))
    session_id = Column(Integer, ForeignKey('session.ID'))
    input_id = Column(Integer, ForeignKey('input.ID'))
    input_data = Column(String, nullable=False)
    output = Column(String, nullable=False)
    uuid = Column(String, default=str(uuid.uuid4()), unique=True, nullable=False) # arrgelar
    