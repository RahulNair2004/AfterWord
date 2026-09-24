from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.auth.security import create_access_token, get_password_hash, verify_password
from app.db.database import get_db
from app.models.user import User
from app.schemas.auth import LoginRequest, RegisterRequest, TokenResponse, UserResponse


router = APIRouter(prefix="/auth",tags=["Authentication"])

# Register User
@router.post("/register",response_model=UserResponse,status_code = status.HTTP_201_CREATED)
def register_user(user_data: RegisterRequest, db: Session = Depends(get_db)):
    # Look by email or username using .filter() and .first()
    existing_user = db.query(User).filter(
        (User.email == user_data.email) | 
        (User.username == user_data.username)
    ).first()
    
    # Choose HTTP_400_BAD_REQUEST for duplicate errors
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username or email already registered."
        )

    # Hash Incoming password from users
    hashed_password = get_password_hash(user_data.password)
    
    # Create the new user instance
    new_user = User(
        username=user_data.username,
        email=user_data.email,
        password_hash=hashed_password
    )
    
    # Add and commit the new database instance
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Return new_user
    return new_user

# Login User
@router.post("/login",response_model=TokenResponse)
def login_user(credentials: LoginRequest,db:Session =  Depends(get_db)):
    # Exception for all errors
    auth_exception  = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail = "Incorrect email or password",
        headers = {"WWW-Authenticate":"Bearer"},
    )

    # Find the user by email
    user = db.query(User).filter(User.email == credentials.email).first()
    if user is None:
        raise auth_exception

    # Verify the password against stored hash
    is_valid = verify_password(credentials.password,user.password_hash)
    if not is_valid:
        raise auth_exception

    # Generate the JWT access token user_id payload
    token_data = {"user_id":user.id}
    jwt_token = create_access_token(data=token_data)

    # Return the TokenResponse mapping 
    return {
        "access_token":jwt_token,
        "token_type":"bearer"
    }

# Get Me
@router.get("/me",response_model=UserResponse)
def read_current_user(current_user: User = Depends(get_current_user)):

    return current_user