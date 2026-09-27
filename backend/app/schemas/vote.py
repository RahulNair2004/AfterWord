from pydantic import BaseModel, Field

class VoteCreateRequest(BaseModel):
    # Enforces that only "up" or "down" can be sent
    vote_type: str = Field(..., pattern="^(up|down)$")
