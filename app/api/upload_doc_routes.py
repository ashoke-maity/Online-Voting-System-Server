from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.core.auth import get_current_admin
from app.database.session import get_db
from app.models.admin import Admin
from app.schemas.uploaded_doc_schema import UploadedDocumentResponse
from app.services.upload_doc import UploadedDocumentService


router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.post(
    "/upload",
    response_model=UploadedDocumentResponse,
    status_code=201
)
def upload_document(
    voter_id: int = Form(...),
    document_type: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin)
):
    try:
        return UploadedDocumentService.upload_document(
            db=db,
            voter_id=voter_id,
            document_type=document_type,
            file=file
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )