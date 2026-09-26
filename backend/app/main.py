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
from app.routes.auth import router as auth_router
from app.routes.users import router as users_router
from app.routes.cases import router as cases_router
from app.routes.evidences import router as evidence_router
from app.routes.theory import router as theories_router


app = FastAPI(
    title="AfterWords API",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(cases_router)
app.include_router(evidence_router)
app.include_router(theories_router)

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