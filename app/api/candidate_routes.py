from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.core.auth import get_current_admin
from app.models.admin import Admin

from app.schemas.candidate_schema import (
    CandidateCreate,
    CandidateUpdate,
    CandidateResponse
)

from app.services.candidate_services import CandidateService


router = APIRouter(
    prefix="/candidates",
    tags=["Candidates"]
)


@router.post(
    "/",
    response_model=CandidateResponse,
    status_code=201
)
def create_candidate(
    candidate: CandidateCreate,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin)
):
    try:
        return CandidateService.create_candidate(
            db,
            candidate
        )
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[CandidateResponse]
)
def get_all_candidates(
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin)
):
    return CandidateService.get_all_candidates(db)


@router.get(
    "/election/{election_id}",
    response_model=list[CandidateResponse]
)
def get_candidates_by_election(
    election_id: int,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin)
):
    try:
        return CandidateService.get_candidates_by_election(
            db,
            election_id
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.get(
    "/{candidate_id}",
    response_model=CandidateResponse
)
def get_candidate(
    candidate_id: int,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin)
):
    try:
        return CandidateService.get_candidate(
            db,
            candidate_id
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.put(
    "/{candidate_id}",
    response_model=CandidateResponse
)
def update_candidate(
    candidate_id: int,
    candidate: CandidateUpdate,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin)
):
    try:
        return CandidateService.update_candidate(
            db,
            candidate_id,
            candidate
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.delete(
    "/{candidate_id}"
)
def delete_candidate(
    candidate_id: int,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin)
):
    try:
        return CandidateService.delete_candidate(
            db,
            candidate_id
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )