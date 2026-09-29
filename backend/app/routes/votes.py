from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.db.database import get_db
from app.models import Theory, Vote, User
from app.schemas.vote import VoteCreateRequest

router = APIRouter(prefix="", tags=["Votes"])

# Cast or modify a vote
@router.post("/theories/{theory_id}/vote", status_code=status.HTTP_200_OK)
def cast_vote(
    theory_id: int,
    vote_data: VoteCreateRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Verify theory exists
    theory = db.query(Theory).filter(Theory.id == theory_id).first()
    if theory is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Theory not found"
        )

    # Check for an existing vote by this specific user on this specific theory
    existing_vote = db.query(Vote).filter(
        Vote.theory_id == theory_id,
        Vote.user_id == current_user.id
    ).first()

    if existing_vote:
        # Update the existing vote type if it changed
        existing_vote.vote_type = vote_data.vote_type
        db.commit()
        db.refresh(existing_vote)
        return {"message": "Vote updated successfully"}
    
    # Create a fresh vote record if none existed
    new_vote = Vote(
        theory_id=theory_id,
        user_id=current_user.id,
        vote_type=vote_data.vote_type
    )
    db.add(new_vote)
    db.commit()
    return {"message": "Vote cast successfully"}

# Remove a vote 
@router.delete("/theories/{theory_id}/vote", status_code=status.HTTP_200_OK)
def delete_vote(
    theory_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    vote = db.query(Vote).filter(
        Vote.theory_id == theory_id,
        Vote.user_id == current_user.id
    ).first()

    if vote is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vote not found"
        )

    db.delete(vote)
    db.commit()
    return {"message": "Vote removed successfully"}

# Aggregate vote tallies 
@router.get("/theories/{theory_id}/votes")
def get_theory_votes(theory_id: int, db: Session = Depends(get_db)):
    theory = db.query(Theory).filter(Theory.id == theory_id).first()
    if theory is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Theory not found"
        )

    # Efficiently count values directly in the database using .count()
    upvotes = db.query(Vote).filter(Vote.theory_id == theory_id, Vote.vote_type == "up").count()
    downvotes = db.query(Vote).filter(Vote.theory_id == theory_id, Vote.vote_type == "down").count()

    return {
        "upvotes": upvotes,
        "downvotes": downvotes
    }
