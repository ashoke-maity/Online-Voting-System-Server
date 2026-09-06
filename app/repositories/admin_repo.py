from sqlalchemy.orm import Session

from app.models.admin import Admin


class AdminRepository:

    @staticmethod
    def create_admin(db: Session, admin: Admin):
        db.add(admin)
        db.commit()
        db.refresh(admin)
        return admin

    @staticmethod
    def get_admin_by_id(db: Session, admin_id: int):
        return (
            db.query(Admin)
            .filter(Admin.admin_id == admin_id)
            .first()
        )

    @staticmethod
    def get_admin_by_email(db: Session, email: str):
        return (
            db.query(Admin)
            .filter(Admin.email == email)
            .first()
        )

    @staticmethod
    def get_all_admins(db: Session):
        return db.query(Admin).all()

    @staticmethod
    def delete_admin(db: Session, admin: Admin):
        db.delete(admin)
        db.commit()