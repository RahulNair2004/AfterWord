from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

class EvidenceCreateRequest(BaseModel):
    title: str
    description: str
    evidence_type: str     # e.g., 'image', 'video', 'document', 'text'

class EvidenceResponse(BaseModel):
    model_config = ConfigDict(from_attributes = True)

    id: int
    case_id: int
    title: str
    description: str
    evidence_type: str
    created_at: datetime