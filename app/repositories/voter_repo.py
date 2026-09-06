from sqlalchemy.orm import Session

from app.models.voter import Voter


class VoterRepository:

    @staticmethod
    def create_voter(
        db: Session,
        voter: Voter
    ):
        db.add(voter)
        db.commit()
        db.refresh(voter)

        return voter

    @staticmethod
    def get_all_voters(db: Session):
        return db.query(Voter).all()

    @staticmethod
    def get_voter_by_id(
        db: Session,
        voter_id: int
    ):
        return (
            db.query(Voter)
            .filter(Voter.voter_id == voter_id)
            .first()
        )

    @staticmethod
    def get_voter_by_email(
        db: Session,
        email: str
    ):
        return (
            db.query(Voter)
            .filter(Voter.email == email)
            .first()
        )

    @staticmethod
    def get_voter_by_phone(
        db: Session,
        phone: str
    ):
        return (
            db.query(Voter)
            .filter(Voter.phone == phone)
            .first()
        )

    @staticmethod
    def update_voter(
        db: Session,
        voter: Voter
    ):
        db.commit()
        db.refresh(voter)

        return voter

    @staticmethod
    def delete_voter(
        db: Session,
        voter: Voter
    ):
        db.delete(voter)
        db.commit()