from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services.AI.service import generate_case_summary, generate_evidence_analysis, generate_theory_analysis, generate_investigation_assistant, generate_paradox_ai
from app.services.AI.schemas import CaseSummaryResponse, EvidenceAnalysisResponse, TheoryAnalysisResponse, InvestigationAssistantRequest, InvestigationAssistantResponse, ParadoxMessage, ParadoxAIResponse


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
    
    except RuntimeError as re:
        raise HTTPException(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        detail=str(re)
        )
    
    except Exception:
        # Prevent leaking connection drops while keeping a safe fallback
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred during AI processing"
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
    except RuntimeError as re:
            raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(re)
            )
    except Exception:
        # Catchign unexpected errors
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexcpected error occured during AI processing."
        )

# Defining endpoints for ai-generated theory analysis
@router.get("/theories/{theory_id}/analysis",response_model = TheoryAnalysisResponse)
def get_theory_analysis(theory_id:int,db:Session = Depends(get_db)):

    try:
        # Offloading structured logic to this layer
        theory_report = generate_theory_analysis(theory_id = theory_id, db=db)

        return theory_report

    except ValueError as ve:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = str(ve)
        )
    except RuntimeError as re:
            raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(re)
        )
    except Exception:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = f"An unexpected error occurred during AI processing."
        )

# Defining the endpoint for ai-generated investigation analysis
@router.post("/cases/{case_id}/assistant",response_model = InvestigationAssistantResponse)
def get_investigation_assistant(case_id: int,payload: InvestigationAssistantRequest, db:Session = Depends(get_db)):

    try:
        # Structuring the context logic to this layer
        investigation_report = generate_investigation_assistant(case_id=case_id, question=payload.question,db=db)

        return investigation_report

    except ValueError as ve:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = str(ve)
        )
    except RuntimeError as re:
            raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(re)
        )
    except Exception:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = f"An unexpected error occurred during AI processing."
        )

# Defining the endpoints for paradox ai analysis
@router.post("/cases/{case_id}/paradox",response_model = ParadoxAIResponse)
def get_paradox_ai(case_id: int, messages: list[ParadoxMessage], db:Session = Depends(get_db)):

    try:
        # Structuring the context logic to this layer
        paradox_report = generate_paradox_ai(case_id = case_id,messages = messages, db=db)

        return paradox_report
    
    except ValueError as ve:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = str(ve)
        )
    except RuntimeError as re:
            raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(re)
        )
    except Exception:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = f"An unexpected error occurred during AI processing."
        )