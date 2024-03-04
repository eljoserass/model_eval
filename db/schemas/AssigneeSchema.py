from pydantic import BaseModel
from db.schemas.OutputSchema import OutputShow
from pydantic import EmailStr

class AssigneeCreate(BaseModel):
    name: str
    email: EmailStr
    
class AssigneeShow(AssigneeCreate):
    outputs: list[OutputShow]