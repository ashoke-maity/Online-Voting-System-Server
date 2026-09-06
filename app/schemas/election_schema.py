from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict


ElectionStatus = Literal[
    "UPCOMING",
    "ACTIVE",
    "COMPLETED",
    "CANCELLED"
]


class ElectionCreate(BaseModel):
    title: str
    start_date: datetime
    end_date: datetime
    status: ElectionStatus


class ElectionUpdate(BaseModel):
    title: str
    start_date: datetime
    end_date: datetime
    status: ElectionStatus


class ElectionResponse(BaseModel):
    election_id: int
    title: str
    start_date: datetime
    end_date: datetime
    status: ElectionStatus

    model_config = ConfigDict(from_attributes=True)