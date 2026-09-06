from sqlalchemy.orm import Session

from app.models.uploadDoc import UploadedDocument


class UploadedDocumentRepository:

    @staticmethod
    def create_document(db: Session, document: UploadedDocument):
        db.add(document)
        db.commit()
        db.refresh(document)
        return document

    @staticmethod
    def get_document_by_id(db: Session, document_id: int):
        return (
            db.query(UploadedDocument)
            .filter(UploadedDocument.document_id == document_id)
            .first()
        )

    @staticmethod
    def get_documents_by_voter(db: Session, voter_id: int):
        return (
            db.query(UploadedDocument)
            .filter(UploadedDocument.voter_id == voter_id)
            .all()
        )

    @staticmethod
    def get_document_by_number(db: Session, document_number: str):
        return (
            db.query(UploadedDocument)
            .filter(UploadedDocument.document_number == document_number)
            .first()
        )

    @staticmethod
    def delete_document(db: Session, document: UploadedDocument):
        db.delete(document)
        db.commit()