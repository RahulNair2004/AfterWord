from pydantic import BaseModel

class CaseSummaryResponse(BaseModel):
    summary: str
    key_facts: list[str]
    unresolved_questions: list[str]

class EvidenceAnalysisResponse(BaseModel):
    summary:str
    significance: str
    possible_connections: list[str]
    questions: list[str]