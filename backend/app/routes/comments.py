from fastapi import HTTPException, APIRouter,Depends,status
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.db.database import get_db
from app.models import Case, Comment, User
from app.schemas.comment import CommentCreateRequest, CommentResponse

router = APIRouter(prefix = "",tags = ["Comments"])

# Post a Comment on a case
@router.post("/cases/{case_id}/comments",response_model = CommentResponse,status_code = status.HTTP_201_CREATED)
def create_comment(case_id: int,comment_data:CommentCreateRequest, current_user: User = Depends(get_current_user),db:Session = Depends(get_db)):
    # Querying the database for Case using id
    case = db.query(Case).filter(Case.id == case_id).first()

    if case is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Case Not Found"
        )

    # Instantiating Comments
    new_comments = Comment(
        case_id = case_id,
        user_id = current_user.id,
        content = comment_data.content
    )

    db.add(new_comments)
    db.commit()
    db.refresh(new_comments)

    return new_comments


# Get all comments for a case

@router.get("/cases/{case_id}/comments",response_model = list[CommentResponse])
def get_case_comments(case_id: int, db:Session = Depends(get_db)):
    case = db.query(Case).filter(Case.id == case_id).first()
    if case is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Case Not Found"
        )

    # Filtering comments using case_id to fetch all
    comments = db.query(Comment).filter(Comment.case_id == case_id).order_by(Comment.created_at.asc()).all()
    return comments

# Get a single comment by ID
@router.get("/comments/{comment_id}",response_model = CommentResponse)
def get_single_comment(comment_id: int,db:Session = Depends(get_db)):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()

    if comment is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Comment Not Found"
        )

    return comment
