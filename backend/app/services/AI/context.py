from sqlalchemy.orm import Session
from app.models import Case, Evidence, Theory
from app.services.AI.schemas import ParadoxMessage

from typing import Optional,List

def build_case_ai_context(case_id: int, db: Session) -> Optional[str]:
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

def build_evidence_ai_context(evidence_id: int,db: Session) -> Optional[str]:

    # Looking at the specific piece of evidence
    evidence = db.query(Evidence).filter(Evidence.id == evidence_id).first()
    if not evidence:
        return None
    
    #  Looking up to the case using foriegn key relationship
    case = db.query(Case).filter(Case.id == evidence.case_id).first()
    if not case:
        return None

    # Extracting historical surrounding clues and theories
    other_evidence = db.query(Evidence).filter(
        Evidence.case_id == case.id,
        Evidence.id != evidence.id
    ).all()

    theories = db.query(Theory).filter(Theory.case_id == case.id).all()

    # Structuring the available data 
    context = "EVIDENCE PROFILE UNDER ANALYSIS\n"
    context += f"Evidence ID: {evidence.id}\n"
    context += f"Title: {evidence.title}\n"
    context += f"Type: {evidence.evidence_type}\n"
    context += f"Description: {evidence.description}\n\n"

    context += "PARENT CASE CONTEXT\n"
    context += f"Case ID: {case.id}\n"
    context += f"Title: {case.title}\n"
    context += f"Category: {case.category}\n"
    context += f"Status: {case.status}\n"
    context += f"Case Description: {case.description}\n\n"

    context += "OTHER EVIDENCE SUBMITTED ON THIS CASE\n"
    if not other_evidence:
        context += "No other evidence has been logged for this case yet.\n"
    else:
        for idx, item in enumerate(other_evidence, 1):
            context += f" Evidence #{idx} [{item.evidence_type}]: {item.title} = {item.description}\n"

    context += "\n"

    context += "EXISTING INVESTIGATOR THEORIES\n"
    if not theories:
        context+="No theories have been submitted by investigator."
    else:
        for idx,item in enumerate(theories,1):
            context += f"Theory #{idx}: {item.content}\n"

    return context

def build_theory_ai_context(theory_id: int, db: Session) -> Optional[str]:

    # Fetching the theory
    theory = db.query(Theory).filter(Theory.id == theory_id).first()

    # If Theory does not exist,return None
    if not theory:
        return None

    # Finding the Parent Case
    case = db.query(Case).filter(Case.id == theory.case_id).first()

    # If Case returns None
    if not case:
        return None

    # Fetching evidence linked to this case and subsequent theories
    evidence_list = db.query(Evidence).filter(Evidence.case_id == case.id).all()

    # Fethcing all theories linked to this case
    theory_list = db.query(Theory).filter(Theory.case_id == case.id, Theory.id != theory.id).all()

    # Constructing the context string

    context = "THEORY UNDER ANALYSIS\n"
    context += f"Theory ID: {theory.id}\n"
    context += f"Theory Content: {theory.content}\n\n"

    context += "PARENT CASE CONTEXT\n"
    context += f"Case ID: {case.id}\n"
    context += f"Title: {case.title}\n"
    context += f"Category: {case.category}\n"
    context += f"Status: {case.status}\n"
    context += f"Case Description: {case.description}\n\n"

    context += "CASE EVIDENCE\n"
    if not evidence_list:
        context += "No evidence has been logged for this case yet.\n"
    else:
        for idx, item in enumerate(evidence_list, 1):
            context += f"Evidence #{idx} [{item.evidence_type}]: {item.title}\n"
            context += f"Details: {item.description}\n\n"

    context += "\n"

    context += "OTHER INVESTIGATOR THEORIES\n"
    if not theory_list:
        context += "No alternative theories have been submitted by other investigators yet.\n"
    else:
        for idx, item in enumerate(theory_list, 1):
            context += f"Alternative Theory #{idx}: {item.content}\n"

    return context

def build_investigation_assistant_context(case_id: int, db: Session) -> Optional[str]:

    # Fetching the case
    case = db.query(Case).filter(Case.id == case_id).first()

    # IF case is None return None
    if not case:
        return None

    # Fetching all evidence linked to the case
    evidence_list = db.query(Evidence).filter(Evidence.case_id == case.id).all()

    # Fethcing theories linked to the case
    theory_list = db.query(Theory).filter(Theory.case_id == case.id).all()

    # Constructing the context string 

    context = "CASE CONTEXT\n"
    context += f"Case ID: {case.id}\n"
    context += f"Title: {case.title}\n"
    context += f"Category: {case.category}\n"
    context += f"Status: {case.status}\n"
    context += f"Description: {case.description}\n\n"

    context += "EVIDENCE\n"
    if not evidence_list:
        context += "No evidence has been logged for this case yet.\n"
    else:
        for idx, item in enumerate(evidence_list, 1):
            context += f"Evidence #{idx}\n"
            context += f"Type: {item.evidence_type}\n"
            context += f"Title: {item.title}\n"
            context += f"Description: {item.description}\n\n"

    context += "INVESTIGATOR THEORIES\n"
    if not theory_list:
        context += "No investigator theories have been submitted for this case yet.\n"
    else:
        for idx, item in enumerate(theory_list, 1):
            context += f"Theory #{idx}\n"
            context += f"Content: {item.content}\n\n"

    return context

def build_paradox_ai_context(case_id: int,messages: list[ParadoxMessage],db:Session) -> Optional[str]:

    # Fetching the case
    case = db.query(Case).filter(Case.id == case_id).first()

    # If case is None return None
    if not case:
        return None

    # Gather Evidence
    evidence_list = db.query(Evidence).filter(Evidence.case_id == case.id).all()

    # Gather Theories
    theory_list = db.query(Theory).filter(Theory.case_id == case.id).all()

    # Constructing the context string 
    context = "CASE CONTEXT\n"
    context += f"Case ID: {case.id}\n"
    context += f"Title: {case.title}\n"
    context += f"Category: {case.category}\n"
    context += f"Status: {case.status}\n"
    context += f"Description: {case.description}\n\n"

    context += "EVIDENCE\n"
    if not evidence_list:
        context += "No evidence has been logged for this case yet.\n"
    else:
        for idx, item in enumerate(evidence_list, 1):
            context += f"Evidence #{idx} [{item.evidence_type}]: {item.title}\n"
            context += f"Details: {item.description}\n\n"

    context += "INVESTIGATOR THEORIES\n"
    if not theory_list:
        context += "No investigator theories have been submitted for this case yet.\n"
    else:
        for idx, item in enumerate(theory_list, 1):
            context += f"Theory #{idx}: {item.content}\n\n"

    # Adding the paradox messages to the context
    context += "PARADOX MESSAGES\n"
    if not messages:
        context += "No active conversations history provided for this case.\n"
    else:
        for msg in messages:
            speaker = "User" if msg.role == "user" else "Assistant"
            context += f"{speaker}: {msg.content}\n"

    return context

