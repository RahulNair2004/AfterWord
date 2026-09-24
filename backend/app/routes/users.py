from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.models.user import User
from app.db.database import get_db
from app.schemas.user import UserPublicResponse,UserUpdateRequest

router  = APIRouter(prefix="/users",tags=["Users"])

# Get Public Profile
@router.get("/{user_id}",response_model=UserPublicResponse)
def get_user_profile(user_id:int ,db: Session=Depends(get_db)):
    # Querying database to find matching user_id
    existing_user = db.query(User).filter(User.id == user_id).first()

    # If no user exists then 404 Not Found
    if existing_user is None:
        raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "User Not Found",
        )

    return existing_user

# Updating the usrname
@router.put("/me",response_model = UserPublicResponse)
def update_username(user_data: UserUpdateRequest,current_user: User=Depends(get_current_user),db:Session = Depends(get_db)):
    # Checking if new requested username is already taken
    username_taken = db.query(User).filter(User.username == user_data.username, User.id!=current_user.id).first()

    # Raise Exception
    if username_taken: 
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "The Username already exists"
        )

    # Creating new username and saving it 
    current_user.username = user_data.username

    # Commiting in the database
    db.commit()
    db.refresh(current_user)

    return current_user
