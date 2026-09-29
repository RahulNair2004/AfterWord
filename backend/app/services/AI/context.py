from sqlalchemy.orm import Session
from app.models import Case, Evidence, Theory

def build_case_ai_context(case_id: int, db: Session):
    """ Query db for specific case and collecting therories and evidence"""
    # Fetch the core case details

    case = db.query(Case).filter(Case.id == case_id).first()

    if not case:
        return None

    # Fetch all evidence rows linked to case
    evidence_list = db.query(Evidence).filter(Evidence.case_id == case_id).all()

    # Fetch all theory entries submitted by users
    theory_list = db.query(Theory).filter(Theory.case_id == case_id).all()

    # Construct structured text string
    context = "CASE DETAILS\n"
    context += f"ID: {case.id}\n"
    context += f"Title: {case.title}\n"
    context += f"Category: {case.category}\n"
    context += f"Status: {case.status}\n"
    context += f"Description: {case.description}\n\n"


    if not evidence_list:
        context+="No Evidence has been logged for this case."
    else:
        for idx,item in enumerate(evidence_list,1):
            context += f"Evidence #{idx} [{item.evidence_type}]: {item.title}\n"
            context += f"Details: {item.description}\n\n"

    context += f"SUBMITTED THEORIES ({len(theory_list)})\n"

    if not theory_list:
        context += "No User Theories have been submitted for this case yet."

    else:
        for idx,item in enumerate(theory_list,1):
            context += f"Theory {idx}:{item.content}\n"

    return context