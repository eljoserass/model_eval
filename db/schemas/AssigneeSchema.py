from pydantic import BaseModel
from db.schemas.OutputSchema import OutputShow

class AssigneeCreate(BaseModel):
    name: str
    
class AssigneeShow(AssigneeCreate):
    outputs: list[OutputShow]