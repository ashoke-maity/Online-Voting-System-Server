from sqlalchemy.orm import Session

from app.models.candidate import Candidate
from app.repositories.candidate_repo import CandidateRepository
from app.repositories.election_repo import ElectionRepository
from app.schemas.candidate_schema import (
    CandidateCreate,
    CandidateUpdate
)


class CandidateService:

    @staticmethod
    def create_candidate(
        db: Session,
        candidate_data: CandidateCreate
    ):

        # Check whether election exists
        election = ElectionRepository.get_election_by_id(
            db,
            candidate_data.election_id
        )

        if not election:
            raise ValueError(
                "Election not found."
            )

        candidate = Candidate(
            election_id=candidate_data.election_id,
            candidate_name=candidate_data.candidate_name,
            party=candidate_data.party,
            symbol=candidate_data.symbol,
            constituency=candidate_data.constituency,
            photo=candidate_data.photo
        )

        return CandidateRepository.create_candidate(
            db,
            candidate
        )

    @staticmethod
    def get_all_candidates(db: Session):

        return CandidateRepository.get_all_candidates(db)

    @staticmethod
    def get_candidate(
        db: Session,
        candidate_id: int
    ):

        candidate = CandidateRepository.get_candidate_by_id(
            db,
            candidate_id
        )

        if not candidate:
            raise ValueError(
                "Candidate not found."
            )

        return candidate

    @staticmethod
    def get_candidates_by_election(
        db: Session,
        election_id: int
    ):

        election = ElectionRepository.get_election_by_id(
            db,
            election_id
        )

        if not election:
            raise ValueError(
                "Election not found."
            )

        return CandidateRepository.get_candidates_by_election(
            db,
            election_id
        )

    @staticmethod
    def update_candidate(
        db: Session,
        candidate_id: int,
        candidate_data: CandidateUpdate
    ):

        candidate = CandidateRepository.get_candidate_by_id(
            db,
            candidate_id
        )

        if not candidate:
            raise ValueError(
                "Candidate not found."
            )

        # Check new election exists
        election = ElectionRepository.get_election_by_id(
            db,
            candidate_data.election_id
        )

        if not election:
            raise ValueError(
                "Election not found."
            )

        candidate.election_id = candidate_data.election_id
        candidate.candidate_name = candidate_data.candidate_name
        candidate.party = candidate_data.party
        candidate.symbol = candidate_data.symbol
        candidate.constituency = candidate_data.constituency
        candidate.photo = candidate_data.photo

        db.commit()
        db.refresh(candidate)

        return candidate

    @staticmethod
    def delete_candidate(
        db: Session,
        candidate_id: int
    ):

        candidate = CandidateRepository.get_candidate_by_id(
            db,
            candidate_id
        )

        if not candidate:
            raise ValueError(
                "Candidate not found."
            )

        CandidateRepository.delete_candidate(
            db,
            candidate
        )

        return {
            "message": "Candidate deleted successfully."
        }