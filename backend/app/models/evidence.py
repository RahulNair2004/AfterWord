from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func

from app.db.database import Base


class Evidence(Base):
    __tablename__ = "evidence"

    id = Column(Integer, primary_key=True, index=True)

    case_id = Column(
        Integer,
        ForeignKey("cases.id"),
        nullable=False
    )

    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)

    evidence_type = Column(String(100))

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )