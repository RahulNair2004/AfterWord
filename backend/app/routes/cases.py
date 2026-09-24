from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.db.database import get_db
from app.models import Case  
from app.schemas.case import CaseCreateRequest, CaseResponse
from app.models import User

router = APIRouter(prefix="/cases",tags=["Cases"])

# Creating New Cases
@router.post("",response_model=CaseResponse,status_code = status.HTTP_201_CREATED)
def create_case(case_data: CaseCreateRequest,current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    # Create the new case instance
    new_case = Case(
        title=case_data.title,
        description = case_data.description,
        category = case_data.category,
        status = "open"
    )

    # Saving in the db
    db.add(new_case)
    db.commit()
    db.refresh(new_case)

    return new_case

# Get all the Case
@router.get("",response_model = list[CaseResponse])
def get_all_cases(db: Session = Depends(get_db)):
    # Quering all cases from database
    cases = db.query(Case).all()
    return cases

# Get Single Cases
@router.get("/{case_id}",response_model = CaseResponse)
def get_single_case(case_id: int,db: Session = Depends(get_db)):
    # Finding specified case by its ID
    case = db.query(Case).filter(Case.id == case_id).first()

    # Check if case exists
    if case is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail="Case Not Found"
        )

    return case