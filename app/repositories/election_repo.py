from sqlalchemy.orm import Session

from app.models.election import Election


class ElectionRepository:

    @staticmethod
    def create_election(
        db: Session,
        election: Election
    ):
        db.add(election)
        db.commit()
        db.refresh(election)

        return election

    @staticmethod
    def get_all_elections(db: Session):
        return db.query(Election).all()

    @staticmethod
    def get_election_by_id(
        db: Session,
        election_id: int
    ):
        return (
            db.query(Election)
            .filter(Election.election_id == election_id)
            .first()
        )

    @staticmethod
    def delete_election(
        db: Session,
        election: Election
    ):
        db.delete(election)
        db.commit()