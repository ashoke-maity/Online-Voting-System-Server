from pydantic import BaseModel, ConfigDict


class CandidateCreate(BaseModel):
    election_id: int
    candidate_name: str
    party: str
    symbol: str
    constituency: str
    photo: str


class CandidateUpdate(BaseModel):
    election_id: int
    candidate_name: str
    party: str
    symbol: str
    constituency: str
    photo: str


class CandidateResponse(BaseModel):
    candidate_id: int
    election_id: int
    candidate_name: str
    party: str
    symbol: str
    constituency: str
    photo: str

    model_config = ConfigDict(from_attributes=True)