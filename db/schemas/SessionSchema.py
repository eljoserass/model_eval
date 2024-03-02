from pydantic import BaseModel

class SessionCreate(BaseModel):
    name: str
    
class SessionShow(SessionCreate):
    pass