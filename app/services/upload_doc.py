import os
import uuid
from datetime import datetime

from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.models.uploadDoc import UploadedDocument
from app.repositories.uploaded_doc_repo import UploadedDocumentRepository
from app.repositories.voter_repo import VoterRepository


UPLOAD_DIR = "uploads/documents"


class UploadedDocumentService:

    @staticmethod
    def upload_document(
        db: Session,
        voter_id: int,
        document_type: str,
        document_number: str,
        file: UploadFile
    ):
        # Check voter exists
        voter = VoterRepository.get_voter_by_id(db, voter_id)

        if not voter:
            raise ValueError("Voter not found.")

        # Check document number already exists
        existing_document = (
            UploadedDocumentRepository.get_document_by_number(
                db, document_number
            )
        )

        if existing_document:
            raise ValueError("A document with this number already exists.")

        # Validate file type
        allowed_extensions = {".jpg", ".jpeg", ".png"}

        original_extension = os.path.splitext(file.filename or "")[1].lower()

        if original_extension not in allowed_extensions:
            raise ValueError(
                "Invalid file type. Only JPG, JPEG and PNG files are allowed."
            )

        # Create upload directory
        os.makedirs(UPLOAD_DIR, exist_ok=True)

        # Generate unique filename
        filename = f"{uuid.uuid4()}{original_extension}"

        file_path = os.path.join(UPLOAD_DIR, filename)

        # Save file
        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())

        # Create database record
        document = UploadedDocument(
            voter_id=voter_id,
            document_type=document_type,
            document_number=document_number,
            document_image_path=file_path,
            created_at=datetime.now()
        )

        try:
            return UploadedDocumentRepository.create_document(
                db, document
            )

        except Exception:
            # Remove uploaded file if database insertion fails
            if os.path.exists(file_path):
                os.remove(file_path)

            raise