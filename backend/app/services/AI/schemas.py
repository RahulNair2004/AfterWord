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

class InvestigationAssistantResponse(BaseModel):
    answer:str
    key_points:list[str]
    follow_up_questions:list[str]

class InvestigationAssistantRequest(BaseModel):
    question:str

class ParadoxMessage(BaseModel):
    role: str
    content: str

class ParadoxAIResponse(BaseModel):
    challenge: str
    alternative_explanations: list[str]
    supporting_points: list[str]
    counter_questions: list[str]