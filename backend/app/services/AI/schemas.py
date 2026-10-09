from pydantic import BaseModel,Field,field_validator,ValidationInfo
from typing import Literal, List

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
    question:str = Field(...,min_length = 1, max_length = 2000)

    # Attaching the validation method right inside the model
    
    @field_validator("question")
    @classmethod
    def validate_whitespace(cls,value:str) -> str:
        stripped_value = value.strip()

        if not stripped_value:
            raise ValueError("Question cannot consist of whitespace.")

        return stripped_value

    
class ParadoxMessage(BaseModel):
    role: Literal["user","assistant"]
    content: str = Field(...,min_length=1,max_length=2000)

    @field_validator("content")
    @classmethod

    def validate_whitespace(cls,value: str):
        stripped_value = value.strip()

        if not stripped_value:
            raise ValueError("Message content cannot consist of whitespace only.")

        return stripped_value
    
class ParadoxAIResponse(BaseModel):
    challenge: str
    alternative_explanations: list[str]
    supporting_points: list[str]
    counter_questions: list[str]