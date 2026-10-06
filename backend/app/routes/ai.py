from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services.AI.service import generate_case_summary, generate_evidence_analysis
from app.services.AI.schemas import CaseSummaryResponse, EvidenceAnalysisResponse


# Initialize router 
router = APIRouter(prefix="/ai", tags=["AI"])

# Defining endpoints for ai-generated case summaries
@router.get("/cases/{case_id}/summary", response_model=CaseSummaryResponse)
def get_case_summary(case_id: int, db: Session = Depends(get_db)):
    
    try:
        # Offload structural processing to your thin service engine
        summary_report = generate_case_summary(case_id=case_id, db=db)
        return summary_report
        
    except ValueError as ve:
        # Safely catch missing database item
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(ve)
        )
    except Exception as e:
        # Prevent leaking connection drops while keeping a safe fallback
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred during AI processing: {str(e)}"
        )

# Defining endpoints for ai-generated evidence analysis
@router.get("/evidence/{evidence_id}/analysis",response_model=EvidenceAnalysisResponse)
def get_evidence_analysis(evidence_id:int,db:Session = Depends(get_db)):

    try:
        # Offloading structured logic to this layer
        analysis_report = generate_evidence_analysis(evidence_id = evidence_id,db=db)

        return analysis_report
    except ValueError as ve:
        # Catching errors
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail=str(ve)
        )

    except Exception as e:
        # Catchign unexpected errors
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexcpected error occured during AI processing {str(e)}"
        )