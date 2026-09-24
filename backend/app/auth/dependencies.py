from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.auth.security import decode_access_token
from app.db.database import get_db
from app.models.user import User


security_scheme = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security_scheme),
                     db: Session = Depends(get_db)) -> User:

    # TO Handle all exceptions we use HTTPException

    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Could Not validate credentials",
        headers = {"WWW-Authenticate":"Bearer"},
    )

    # Extract and Decode the Token

    # Extract string token from scheme

    token = credentials.credentials

    # Decode the token using security.py 

    payload = decode_access_token(token)

    if payload is None:
        raise credentials_exception

    # Extract user ID from payload

    user_id = payload.get("user_id")
    if user_id is None or not isinstance(user_id, int):
        raise credentials_exception

    # Querying the database and return the user

    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise credentials_exception

    # Return the authenticated SQLAlchemy User

    return user