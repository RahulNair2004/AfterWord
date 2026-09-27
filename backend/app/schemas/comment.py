from datetime import datetime
from pydantic import BaseModel, ConfigDict

class CommentCreateRequest(BaseModel):
    content:str

class CommentResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    case_id: int
    content: str
    created_at: datetime