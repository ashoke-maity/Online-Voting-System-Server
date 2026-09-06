from datetime import datetime

from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.models.admin import Admin
from app.repositories.admin_repo import AdminRepository
from app.schemas.admin_schema import AdminCreate, AdminLogin
from app.core.security import create_access_token


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AdminService:

    # admin creation method

    @staticmethod
    def create_admin(db: Session, admin_data: AdminCreate):

        existing_admin = AdminRepository.get_admin_by_email(
            db,
            admin_data.email
        )

        if existing_admin:
            raise ValueError("Admin with this email already exists.")

        hashed_password = pwd_context.hash(admin_data.password)

        admin = Admin(
            name=admin_data.name,
            email=admin_data.email,
            password_hash=hashed_password,
            role="ADMIN",
            created_at=datetime.now()
        )

        return AdminRepository.create_admin(db, admin)

# admin login method

    @staticmethod
    def login_admin(
        db: Session,
        admin_data: AdminLogin
    ):

        admin = AdminRepository.get_admin_by_email(
            db,
            admin_data.email
        )

        if not admin:
            raise ValueError(
                "Invalid email or password."
            )

        password_valid = pwd_context.verify(
            admin_data.password,
            admin.password_hash
        )

        if not password_valid:
            raise ValueError(
                "Invalid email or password."
            )

        access_token = create_access_token({
            "sub": str(admin.admin_id),
            "role": admin.role
        })

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }