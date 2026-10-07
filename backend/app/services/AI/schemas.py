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

class TheoryAnalysisResponse(BaseModel):
    summary: str
    supporting_evidence: list[str]
    contradictions: list[str]
    questions: list[str]