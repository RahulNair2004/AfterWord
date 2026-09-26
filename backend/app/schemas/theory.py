from datetime import datetime
from pydantic import BaseModel, ConfigDict

class TheoryCreateRequest(BaseModel):
    content: str

class TheoryResponse(BaseModel):
    model_config = ConfigDict(from_attributes = True)

    id: int
    case_id: int
    user_id: int
    content: str
    created_at: datetime
