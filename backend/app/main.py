from fastapi import FastAPI
from sqlalchemy import text

from app.db.database import engine, Base
from app.models import (
    User,
    Case,
    Evidence,
    Theory,
    Comment,
    Vote
)

app = FastAPI(
    title="AfterWords API",
    version="1.0.0"
)


Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {
        "message": "AfterWords API is running"
    }


@app.get("/health")
def health():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "status": "healthy",
            "database": "connected"
        }

    except Exception as e:
        return {
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(e)
        }