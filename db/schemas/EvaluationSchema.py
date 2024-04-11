from pydantic import BaseModel
from db.schemas.OutputSchema import OutputShow
from pydantic import EmailStr

class EvaluationCreate(BaseModel):
    assignee_output_id: int
    q1: int
    q2: int
    q3: int
    q4: str