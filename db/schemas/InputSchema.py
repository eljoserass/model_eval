from pydantic import BaseModel
from db.schemas.OutputSchema import OutputShow

class InputCreate(BaseModel):
    data: str
    
class InputShow(InputCreate):
    outputs: list[OutputShow]