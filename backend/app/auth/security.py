from datetime import datetime,timedelta,timezone
import os
from typing import Optional

from passlib.context import CryptContext
import jwt
from jwt.exceptions import InvalidTokenError, ExpiredSignatureError

from dotenv import load_dotenv

# Load environment configuration
load_dotenv()

# Configuration Settings

SECRET_KEY = os.environ.get("JWT_SECRET")
ALGORITHM = "HS256"
DEFAULT_ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Initializing Passlib's CryptContext
pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

def get_password_hash(password: str) -> str:

    return pwd_context.hash(password)

def verify_password(plain_password: str,hashed_password: str) -> bool:

    return pwd_context.verify(plain_password, hashed_password)

# JWT Initialization 
def create_access_token(data:dict, expires_delta: Optional[timedelta]=None) -> str:

    # Creating a copy of data 
    to_encode = data.copy()

    # Calculate expiration time
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=DEFAULT_ACCESS_TOKEN_EXPIRE_MINUTES
        )

    # Update the payload with expiration
    to_encode.update({"exp":expire})

    # Encode and sign with JWT
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str) -> Optional[dict]:

    # Return the decoded payload dictionary
    try:
        # decode automatically verifies signature and expiration
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except (ExpiredSignatureError, InvalidTokenError):
        # Returns None if the token is expired
        return None