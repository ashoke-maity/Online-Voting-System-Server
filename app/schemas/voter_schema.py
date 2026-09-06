from datetime import date, datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, EmailStr


Gender = Literal[
    "MALE",
    "FEMALE",
    "OTHER"
]

VerificationStatus = Literal[
    "PENDING",
    "VERIFIED",
    "REJECTED"
]


class VoterCreate(BaseModel):
    full_name: str
    father_name: str
    dob: date
    gender: Gender
    phone: str
    email: EmailStr | None = None
    constituency: str | None = None
    face_embeddings_path: str
    face_image_path: str


class VoterUpdate(BaseModel):
    full_name: str
    father_name: str
    dob: date
    gender: Gender
    phone: str
    email: EmailStr | None = None
    constituency: str | None = None
    face_embeddings_path: str
    face_image_path: str


class VoterResponse(BaseModel):
    voter_id: int
    full_name: str
    father_name: str
    dob: date
    gender: Gender
    phone: str
    email: EmailStr | None
    constituency: str | None
    face_embeddings_path: str
    face_image_path: str
    has_voted: bool
    created_by: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)