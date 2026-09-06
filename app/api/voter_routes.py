from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.core.auth import get_current_admin
from app.models.admin import Admin

from app.schemas.voter_schema import (
    VoterCreate,
    VoterUpdate,
    VoterResponse
)

from app.services.voter_services import VoterService


router = APIRouter(
    prefix="/voters",
    tags=["Voters"]
)


@router.post(
    "/",
    response_model=VoterResponse,
    status_code=201
)
def create_voter(
    voter: VoterCreate,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin)
):
    try:
        return VoterService.create_voter(
            db,
            voter,
            current_admin.admin_id
        )
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[VoterResponse]
)
def get_all_voters(
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin)
):
    return VoterService.get_all_voters(db)


@router.get(
    "/{voter_id}",
    response_model=VoterResponse
)
def get_voter(
    voter_id: int,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin)
):
    try:
        return VoterService.get_voter(
            db,
            voter_id
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.put(
    "/{voter_id}",
    response_model=VoterResponse
)
def update_voter(
    voter_id: int,
    voter: VoterUpdate,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin)
):
    try:
        return VoterService.update_voter(
            db,
            voter_id,
            voter
        )
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete(
    "/{voter_id}"
)
def delete_voter(
    voter_id: int,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin)
):
    try:
        return VoterService.delete_voter(
            db,
            voter_id
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )