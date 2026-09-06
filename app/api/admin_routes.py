from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.admin_schema import AdminCreate, AdminResponse, AdminLogin
from app.services.admin_services import AdminService
from app.core.auth import get_current_admin
from app.models.admin import Admin

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.post(
    "/create",
    response_model=AdminResponse,
    status_code=201
)
def create_admin(
    admin: AdminCreate,
    db: Session = Depends(get_db)
):
    try:
        return AdminService.create_admin(db, admin)
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

@router.post("/login")
def admin_login(
    admin: AdminLogin,
    db: Session = Depends(get_db)
):
    try:
        return AdminService.login_admin(db, admin)
    except ValueError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e)
        )

@router.get("/me", response_model=AdminResponse)
def get_my_admin_profile(
    current_admin: Admin = Depends(get_current_admin)
):
    return current_admin