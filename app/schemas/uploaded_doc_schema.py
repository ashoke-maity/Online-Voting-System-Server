from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict


DocumentType = Literal["AADHAAR", "PAN", "VOTER"]


class UploadedDocumentResponse(BaseModel):
    document_id: int
    voter_id: int
    document_type: DocumentType
    document_number: str
    document_image_path: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)