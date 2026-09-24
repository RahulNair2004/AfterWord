from datetime import datetime
from pydantic import BaseModel,Field,ConfigDict

class CaseCreateRequest(BaseModel):
    title: str
    description: str
    category: str

class CaseResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int
    title:str
    description:str
    category:str
    status:str
    created_at:datetime