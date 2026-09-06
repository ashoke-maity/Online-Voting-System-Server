from datetime import datetime

from sqlalchemy import ForeignKey, Integer, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Vote(Base):
    __tablename__ = "votes"
    __table_args__ = {"schema": "online_voting"}

    vote_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    voter_id: Mapped[int] = mapped_column(
        ForeignKey("online_voting.voters.voter_id"),
        nullable=False
    )

    candidate_id: Mapped[int] = mapped_column(
        ForeignKey("online_voting.candidates.candidate_id"),
        nullable=False
    )

    election_id: Mapped[int] = mapped_column(
        ForeignKey("online_voting.elections.election_id"),
        nullable=False
    )

    timestamp: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        nullable=False
    )