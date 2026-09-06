from datetime import date, datetime

from sqlalchemy import Boolean, Date, ForeignKey, Integer, String, TEXT, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Voter(Base):
    __tablename__ = "voters"
    __table_args__ = {"schema": "online_voting"}

    voter_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    full_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    father_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    dob: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    gender: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    phone: Mapped[str] = mapped_column(
        String(15),
        nullable=False
    )

    email: Mapped[str | None] = mapped_column(
        String(255),
        unique=True,
        nullable=True
    )

    constituency: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    face_embeddings_path: Mapped[str] = mapped_column(
        TEXT,
        nullable=False
    )

    face_image_path: Mapped[str] = mapped_column(
        TEXT,
        nullable=False
    )

    verification_status: Mapped[str] = mapped_column(
        String(30),
        nullable=False
    )

    has_voted: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False
    )

    created_by: Mapped[int] = mapped_column(
        ForeignKey("online_voting.admins.admin_id"),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        nullable=False
    )