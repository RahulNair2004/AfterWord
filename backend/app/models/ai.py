from sqlalchemy import Column,Integer,String,ForeignKey,DateTime,JSON

from sqlalchemy.sql import func
from app.db.database import Base

class AIAnalysis(Base):

    __tablename__ = "ai_analyses"

    id = Column(Integer,primary_key=True,index=True)
    case_id = Column(Integer,ForeignKey("cases.id"),nullable=False)
    evidence_id = Column(Integer,ForeignKey("evidence.id"),nullable=True)
    theory_id = Column(Integer,ForeignKey("theories.id"),nullable=True)
    analysis_type = Column(String(50),nullable=False)
    response = Column(JSON,nullable=False)
    model = Column(String(100),nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now())
    updated_at = Column(DateTime(timezone=True),server_default=func.now(),onupdate=func.now())