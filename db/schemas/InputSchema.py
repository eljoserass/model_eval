from pydantic import BaseModel
from db.schemas.OutputSchema import OutputShow
from db.models.Input import Label

class InputCreate(BaseModel):
    data: str
    label: Label
    
class InputShow(InputCreate):
    outputs: list[OutputShow]