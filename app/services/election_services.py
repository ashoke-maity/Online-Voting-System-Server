from sqlalchemy.orm import Session

from app.models.election import Election
from app.repositories.election_repo import ElectionRepository
from app.schemas.election_schema import ElectionCreate, ElectionUpdate


class ElectionService:

    @staticmethod
    def create_election(
        db: Session,
        election_data: ElectionCreate
    ):

        if election_data.end_date <= election_data.start_date:
            raise ValueError(
                "End date must be after start date."
            )

        election = Election(
            title=election_data.title,
            start_date=election_data.start_date,
            end_date=election_data.end_date,
            status=election_data.status
        )

        return ElectionRepository.create_election(
            db,
            election
        )

    @staticmethod
    def get_all_elections(db: Session):

        return ElectionRepository.get_all_elections(db)

    @staticmethod
    def get_election(
        db: Session,
        election_id: int
    ):

        election = ElectionRepository.get_election_by_id(
            db,
            election_id
        )

        if not election:
            raise ValueError("Election not found.")

        return election

    @staticmethod
    def update_election(
        db: Session,
        election_id: int,
        election_data: ElectionUpdate
    ):

        election = ElectionRepository.get_election_by_id(
            db,
            election_id
        )

        if not election:
            raise ValueError("Election not found.")

        if election_data.end_date <= election_data.start_date:
            raise ValueError(
                "End date must be after start date."
            )

        election.title = election_data.title
        election.start_date = election_data.start_date
        election.end_date = election_data.end_date
        election.status = election_data.status

        db.commit()
        db.refresh(election)

        return election

    @staticmethod
    def delete_election(
        db: Session,
        election_id: int
    ):

        election = ElectionRepository.get_election_by_id(
            db,
            election_id
        )

        if not election:
            raise ValueError("Election not found.")

        ElectionRepository.delete_election(
            db,
            election
        )

        return {
            "message": "Election deleted successfully."
        }