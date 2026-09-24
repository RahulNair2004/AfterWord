from datetime import datetime
from pydantic import BaseModel,ConfigDict,Field

class UserPublicResponse(BaseModel):

    model_config = ConfigDict(from_attributes = True)
    id: int
    username:str
    created_at: datetime

class UserUpdateRequest(BaseModel):

    username: str
