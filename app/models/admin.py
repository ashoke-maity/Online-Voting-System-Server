from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, TIMESTAMP

from app.database.base import Base

# admin table 
class Admin(Base):
    # connecting to already created table in database through DBeaver
    __tablename__ = "admins"
    __table_args__ = {"schema": "online_voting"}

    admin_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[str] = mapped_column(String(20), nullable=False)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False)