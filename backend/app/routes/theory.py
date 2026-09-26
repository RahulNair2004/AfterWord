from fastapi import APIRouter, Depends , HTTPException, status
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.db.database import get_db
from app.models import User, Theory, Case
from app.schemas.theory import TheoryCreateRequest, TheoryResponse

router = APIRouter(tags=["Theory"])

# Post thoeries for cases 
@router.post("/cases/{case_id}/theories",response_model = TheoryResponse,status_code = status.HTTP_201_CREATED)
def create_theories(case_id: int, theory_data: TheoryCreateRequest, current_user: User = Depends(get_current_user),db:Session=Depends(get_db)):

    # Querying the database
    case_exists = db.query(Case).filter(Case.id == case_id).first()

    if case_exists is None:
        raise HTTPException(
            status_code  = status.HTTP_404_NOT_FOUND,
            detail = "case not found"
        )

    # Instantiate the new theory to the payload and url body
    new_theory = Theory(
        case_id = case_id,
        user_id = current_user.id,
        content = theory_data.content
    )

    db.add(new_theory)
    db.commit()
    db.refresh(new_theory)

    return new_theory

# Get all the theory cases
@router.get("/cases/{case_id}/theories", response_model = list[TheoryResponse])
def get_all_theory(case_id: int, db: Session = Depends(get_db)):

    # Check the case exists or not 
    case_exists = db.query(Case).filter(Case.id == case_id).first()

    if case_exists is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail="Case Not Found"
        )

    # Queting the Theory table to fetch theories
    theory = db.query(Theory).filter(Theory.case_id == case_id).order_by(Theory.created_at.asc()).all()

    return theory

# Get the First cases
@router.get("/theories/{theory_id}",response_model = TheoryResponse)
def get_theory(theory_id: int, db: Session = Depends(get_db)):

    # Query the Theory 
    theory_item = db.query(Theory).filter(Theory.id == theory_id).first()

    if theory_item is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Theory is not found"
        )

    return theory_item
    