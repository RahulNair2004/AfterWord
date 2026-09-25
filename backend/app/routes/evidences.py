from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.db.database import get_db
from app.models import Case, Evidence,User
from app.schemas.evidence import EvidenceCreateRequest,EvidenceResponse

router = APIRouter(tags=["Evidence"])

# We have to add evidence to the cases
@router.post("/cases/{case_id}/evidence", response_model = EvidenceResponse,status_code = status.HTTP_201_CREATED)
def add_evidence(case_id: int, evidence_data: EvidenceCreateRequest, db:Session = Depends(get_db),current_user:User = Depends(get_current_user)):

    # Query database using case_Id
    case = db.query(Case).filter(Case.id == case_id).first()

    if case is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail="Case Not Found"
        )

    # Instantiate evidence by combining path variable and request body

    new_evidence = Evidence(
        case_id = case_id,
        title = evidence_data.title,
        description = evidence_data.description,
        evidence_type = evidence_data.evidence_type
    )

    db.add(new_evidence)
    db.commit()
    db.refresh(new_evidence)

    return new_evidence


# Get all evidence for a specific case
@router.get("/cases/{case_id}/evidence", response_model = list[EvidenceResponse])
def get_case_evidence(case_id: int, db:Session = Depends(get_db)):
    # Whether case exists first
    case = db.query(Case).filter(Case.id == case_id).first()
    if case is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Case Not Found"
        )

    # Fetch evidence belonging to this

    evidence_list = db.query(Evidence).filter(Evidence.case_id == case_id).all()
    return evidence_list

# Get a single evidence item by ID
@router.get("/evidence/{evidence_id}",response_model = EvidenceResponse)
def get_single_evidence(evidence_id: int,db:Session = Depends(get_db)):
    # Query Evidence table directly by ID
    evidence_item = db.query(Evidence).filter(Evidence.id == evidence_id).first()

    if evidence_item is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Evidence Not FOund"
        )

    return evidence_item


