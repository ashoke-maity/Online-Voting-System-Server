import os
import uuid
from datetime import datetime

import httpx
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
        file: UploadFile
    ):
        # Check voter exists
        voter = VoterRepository.get_voter_by_id(db, voter_id)

        if not voter:
            raise ValueError("Voter not found.")

        # Validate document type
        allowed_document_types = {
            "AADHAAR",
            "PAN",
            "VOTER"
        }

        if document_type not in allowed_document_types:
            raise ValueError(
                "Invalid document type. Use AADHAAR, PAN or VOTER."
            )

        # Validate file type
        allowed_extensions = {
            ".jpg",
            ".jpeg",
            ".png"
        }

        original_extension = os.path.splitext(
            file.filename or ""
        )[1].lower()

        if original_extension not in allowed_extensions:
            raise ValueError(
                "Invalid file type. Only JPG, JPEG and PNG files are allowed."
            )

        # Create upload directory
        os.makedirs(UPLOAD_DIR, exist_ok=True)

        # Generate unique filename
        filename = f"{uuid.uuid4()}{original_extension}"

        file_path = os.path.join(
            UPLOAD_DIR,
            filename
        )

        # Save uploaded image
        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())

        try:
            # Send image to OCR service
            with open(file_path, "rb") as image_file:

                response = httpx.post(
                    "http://127.0.0.1:8001/ocr/extract",
                    data={
                        "document_type": document_type
                    },
                    files={
                        "file": (
                            filename,
                            image_file,
                            file.content_type
                        )
                    },
                    timeout=300.0
                )

            # Check OCR service response
            if response.status_code != 200:
                raise ValueError(
                    "OCR service failed to process the document."
                )

            # Get OCR result
            ocr_result = response.json()

            extracted_number = ocr_result.get(
                "document_number"
            )

            # OCR couldn't find document number
            if not extracted_number:
                raise ValueError(
                    "Document number could not be detected by OCR."
                )

            # Check duplicate document number
            existing_document = (
                UploadedDocumentRepository
                .get_document_by_number(
                    db,
                    extracted_number
                )
            )

            if existing_document:
                raise ValueError(
                    "A document with this number already exists."
                )

            # Create database record
            document = UploadedDocument(
                voter_id=voter_id,
                document_type=document_type,
                document_number=extracted_number,
                document_image_path=file_path,
                created_at=datetime.now()
            )

            return UploadedDocumentRepository.create_document(
                db,
                document
            )

        except ValueError:
            if os.path.exists(file_path):
                os.remove(file_path)

            raise

        except Exception:
            if os.path.exists(file_path):
                os.remove(file_path)

            raise