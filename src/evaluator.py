"""

will init class with session name, and kwargs for specific models and amount of inputs to run
will sample inputs randomly
will init model_caller
will init ouput_store
will store in db session_id
will loop through list of ids in db and pass it to model caller, with each input
will get output from model_caller and save it through output_store


"""

"""
interesting to add feature that repeats intentionally the input to see if response is deterministically the same
- have to add row to outputs that allow an output to be repeated
"""
from src.model_caller import ModelCalller
from db.daos.ModelDao import ModelDao
from db.daos.OutputDao import OutputDao
from db.schemas.ModelSchema import ModelCreate
from db.daos.SessionDao import SessionDao
from db.schemas.OutputSchema import OutputCreate
from db.schemas.SessionSchema import SessionCreate
from db.schemas.InputSchema import InputCreate

from db.daos.InputDao import InputDao
from db.connector import session

class Evaluator:
    def __init__(self, session_name: str, n_inputs: int | None = None, shuffle: bool = True):
        self.models = ModelDao(session).get_all()
        self.model_caller = ModelCalller()
        self.inputs = InputDao(session).get_with_limit(n_inputs, shuffle=shuffle)
        self.session_id = self.get_session_id(session_name)

    def run_debug(self, inputs: list[InputCreate], models: list[ModelCreate]):
        for model in models:
            for query in inputs:
                response = self.model_caller(model_name=model.name, query=query.data, provider=model.provider)
                print (f"{model.name}:\n{response}")
    
    def get_session_id(self, session_name: str) -> int:
        session_obj = SessionDao(session).get_by_name(name=session_name)
        if session_obj == None:
            SessionDao(session).create(
                SessionCreate(
                    name=session_name
                ).model_dump()
            )
        session_obj = SessionDao(session).get_by_name(name=session_name)
        return session_obj.ID
    
    def run(self,
            force_inputs: list[InputCreate] = None,
            force_models: list[ModelCreate] = None,
            debug: bool = False) -> None:
        
        if debug:
            self.run_debug(models=force_models, inputs=force_inputs)
            return

        for model in self.models:
            
            for query in self.inputs:
                print (f"query={query.data} modelname={model.name}  provider={model.provider}")
                response = self.model_caller(model_name=model.name, query=query.data, provider=model.provider)

                print (f"{model.name}:\n{response}")
                
                OutputDao(session).create(
                    OutputCreate(
                        data=response,
                        model_id=model.ID,
                        session_id=self.session_id,
                        input_id=query.ID
                    ).model_dump())