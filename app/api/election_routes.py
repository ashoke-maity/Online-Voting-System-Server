from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.core.auth import get_current_admin
from app.models.admin import Admin

from app.schemas.election_schema import (
    ElectionCreate,
    ElectionUpdate,
    ElectionResponse
)

from app.services.election_services import ElectionService


router = APIRouter(
    prefix="/elections",
    tags=["Elections"]
)


@router.post(
    "/",
    response_model=ElectionResponse,
    status_code=201
)
def create_election(
    election: ElectionCreate,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin)
):
    try:
        return ElectionService.create_election(
            db,
            election
        )
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[ElectionResponse]
)
def get_all_elections(
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin)
):
    return ElectionService.get_all_elections(db)


@router.get(
    "/{election_id}",
    response_model=ElectionResponse
)
def get_election(
    election_id: int,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin)
):
    try:
        return ElectionService.get_election(
            db,
            election_id
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.put(
    "/{election_id}",
    response_model=ElectionResponse
)
def update_election(
    election_id: int,
    election: ElectionUpdate,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin)
):
    try:
        return ElectionService.update_election(
            db,
            election_id,
            election
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.delete(
    "/{election_id}"
)
def delete_election(
    election_id: int,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin)
):
    try:
        return ElectionService.delete_election(
            db,
            election_id
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )