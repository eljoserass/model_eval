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

from db.connector import get_session

class Evaluator:
    def __init__(self, session_name: str, n_inputs: int | None = None, shuffle: bool = True):
        self.model_caller = ModelCalller()
        self.session_name = session_name
        # with get_session() as db:
        #     self.session_obj = SessionDao(db).get_by_name(session_name)

    def run_debug(self, inputs: list[InputCreate], models: list[ModelCreate], system_prompts: list[str]):
        for prompt in system_prompts:
            for model in models:
                for query in inputs:
                    response = self.model_caller(model_name=model.name, query=query.data, provider=model.provider, system_prompt=prompt)
                    print (f"{model.name}:\n{response}")

    
    def run(self,
            force_inputs: list[InputCreate] = None,
            force_models: list[ModelCreate] = None,
            debug: bool = False) -> None:
        
        if debug:
            self.run_debug(models=force_models, inputs=force_inputs)
            return
        
        with get_session() as db:
            session_obj = SessionDao(db).get_by_name(self.session_name)

            counter = 0

            for system_prompt in session_obj.prompts:
                print (f"SYS\n{system_prompt.data}")
                for model in session_obj.models:
                    for query in session_obj.inputs:
                        print (f"query={query.data} modelname={model.name}  provider={model.provider}")
                        print(f"{counter=}")
                        if not self.model_caller.verify(session_id=session_obj.ID, model_id=model.ID, query_id=query.ID, session_db=db):
                            response = self.model_caller(model_name=model.name, query=query.data, provider=model.provider, system_prompt=system_prompt.data)
                            OutputDao(db).create(
                                    OutputCreate(
                                        data=response,
                                        model_id=model.ID,
                                        session_id=session_obj.ID,
                                        input_id=query.ID
                                ).model_dump())
                        counter += 1