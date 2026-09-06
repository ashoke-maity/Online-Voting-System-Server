from sqlalchemy import ForeignKey, Integer, String, TEXT
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Candidate(Base):
    __tablename__ = "candidates"
    __table_args__ = {"schema": "online_voting"}

    candidate_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    election_id: Mapped[int] = mapped_column(
        ForeignKey("online_voting.elections.election_id"),
        nullable=False
    )

    candidate_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    party: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    symbol: Mapped[str] = mapped_column(
        TEXT,
        nullable=False
    )

    constituency: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    photo: Mapped[str] = mapped_column(
        TEXT,
        nullable=False
    )