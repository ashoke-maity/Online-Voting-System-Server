from datetime import datetime

from sqlalchemy import ForeignKey, Integer, String, TEXT, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class UploadedDocument(Base):
    __tablename__ = "uploaded_documents"
    __table_args__ = {"schema": "online_voting"}

    document_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    voter_id: Mapped[int] = mapped_column(
        ForeignKey("online_voting.voters.voter_id"),
        nullable=False
    )

    document_type: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    document_number: Mapped[str] = mapped_column(
        String(25),
        unique=True,
        nullable=False
    )

    document_image_path: Mapped[str] = mapped_column(
        TEXT,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        nullable=False
    )