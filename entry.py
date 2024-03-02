from db.models.Base import Base
from db.connector import engine
from db.models import Assignee, Input, Model, Output, OutputAssignee, Session
from db.connector import session

Base.metadata.create_all(bind=engine)


from db.models.Model import Provider
from db.daos.ModelDao import ModelDao
from db.schemas.ModelSchema import ModelCreate

from db.daos.OutputDao import OutputDao
from db.schemas.OutputSchema import OutputCreate, OutputShow

from db.daos.InputDao import InputDao
from db.schemas.InputSchema import InputCreate

from db.daos.SessionDao import SessionDao
from db.schemas.SessionSchema import SessionCreate

ModelDao(session).create(ModelCreate(name="Model 1", provider=Provider.POE).model_dump())

InputDao(session).create(InputCreate(data="Input Data").model_dump())

SessionDao(session).create(SessionCreate(name="Session Name").model_dump())

OutputDao(session).create(OutputCreate(data="Output Data", model_id=1, session_id=1, input_id=1).model_dump())

outputs = OutputDao(session).get_all()

for output in outputs:
    print(output)

#print(ModelCreate(name="34432").model_dump())




"""


- how to store responses

technology: sqlite (more confy for relationships)

table for models with their id
table for realtion between model and model responses
table for models responses

- how to get the responses

poe, ollama and replicate api

loop tohrough models table
call model through model_caller with the table model_id
pass answer to response_storer, with the model_id from the table

    
"""