from datetime import datetime

from sqlalchemy import Integer, String, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Election(Base):
    __tablename__ = "elections"
    __table_args__ = {"schema": "online_voting"}

    election_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    start_date: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        nullable=False
    )

    end_date: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )