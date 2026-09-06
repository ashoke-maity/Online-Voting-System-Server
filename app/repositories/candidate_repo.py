from sqlalchemy.orm import Session

from app.models.candidate import Candidate


class CandidateRepository:

    @staticmethod
    def create_candidate(
        db: Session,
        candidate: Candidate
    ):
        db.add(candidate)
        db.commit()
        db.refresh(candidate)

        return candidate

    @staticmethod
    def get_all_candidates(db: Session):
        return db.query(Candidate).all()

    @staticmethod
    def get_candidate_by_id(
        db: Session,
        candidate_id: int
    ):
        return (
            db.query(Candidate)
            .filter(
                Candidate.candidate_id == candidate_id
            )
            .first()
        )

    @staticmethod
    def get_candidates_by_election(
        db: Session,
        election_id: int
    ):
        return (
            db.query(Candidate)
            .filter(
                Candidate.election_id == election_id
            )
            .all()
        )

    @staticmethod
    def delete_candidate(
        db: Session,
        candidate: Candidate
    ):
        db.delete(candidate)
        db.commit()