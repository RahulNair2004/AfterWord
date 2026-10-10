from fastapi import FastAPI
from sqlalchemy import text
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import engine, Base
from app.models import (
    User,
    Case,
    Evidence,
    Theory,
    Comment,
    Vote,
    AIAnalysis
)
from app.routes.auth import router as auth_router
from app.routes.users import router as users_router
from app.routes.cases import router as cases_router
from app.routes.evidences import router as evidence_router
from app.routes.theory import router as theories_router
from app.routes.comments import router as comments_router
from app.routes.votes import router as votes_router
from app.routes.ai import router as ai_router

app = FastAPI(
    title="AfterWords API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(cases_router)
app.include_router(evidence_router)
app.include_router(theories_router)
app.include_router(comments_router)
app.include_router(votes_router)
app.include_router(ai_router)

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