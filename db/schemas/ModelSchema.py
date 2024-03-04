from pydantic import BaseModel
from db.schemas.OutputSchema import OutputShow
from db.models.Model import Provider

class ModelCreate(BaseModel):
    name: str
    provider: Provider
    
class ModelShow(ModelCreate):
    outputs: list[OutputShow]