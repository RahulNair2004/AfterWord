from pydantic import BaseModel

class CaseSummaryResponse(BaseModel):
    summary: str
    key_facts: list[str]
    unresolved_questions: list[str]
