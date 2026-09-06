from datetime import datetime

from sqlalchemy import Boolean, ForeignKey, Integer, Numeric, String, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class VerificationLog(Base):
    __tablename__ = "verification_logs"
    __table_args__ = {"schema": "online_voting"}

    log_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    voter_id: Mapped[int] = mapped_column(
        ForeignKey("online_voting.voters.voter_id"),
        nullable=False
    )

    document_verified: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False
    )

    face_verified: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False
    )

    liveness_verified: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False
    )

    face_match_score: Mapped[float] = mapped_column(
        Numeric(5, 2),
        nullable=False
    )

    verification_type: Mapped[str] = mapped_column(
        String(30),
        nullable=False
    )

    timestamp: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        nullable=False
    )