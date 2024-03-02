from __future__ import annotations
from pydantic import BaseModel, ConfigDict
#from db.schemas.ModelSchema import ModelShow
#from db.schemas.SessionSchema import SessionShow
#from db.schemas.InputSchema import InputShow
#from db.schemas.AssigneeSchema import AssigneeShow


class OutputCreate(BaseModel):
    data: str
    model_id: int
    session_id: int
    input_id: int
    
    model_config = ConfigDict(protected_namespaces=())
    
class OutputShow(OutputCreate):
    model: "ModelShow"
    session: "SessionShow"
    input: "InputShow"
    assignees: list["AssigneeShow"]