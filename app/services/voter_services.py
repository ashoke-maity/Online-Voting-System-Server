from datetime import datetime

from sqlalchemy.orm import Session

from app.models.voter import Voter
from app.repositories.voter_repo import VoterRepository
from app.schemas.voter_schema import VoterCreate, VoterUpdate


class VoterService:

    @staticmethod
    def create_voter(
        db: Session,
        voter_data: VoterCreate,
        admin_id: int
    ):

        # Check duplicate email
        if voter_data.email:
            existing_voter = VoterRepository.get_voter_by_email(
                db,
                voter_data.email
            )

            if existing_voter:
                raise ValueError(
                    "A voter with this email already exists."
                )

        # Check duplicate phone
        existing_voter = VoterRepository.get_voter_by_phone(
            db,
            voter_data.phone
        )

        if existing_voter:
            raise ValueError(
                "A voter with this phone number already exists."
            )

        voter = Voter(
            full_name=voter_data.full_name,
            father_name=voter_data.father_name,
            dob=voter_data.dob,
            gender=voter_data.gender,
            phone=voter_data.phone,
            email=voter_data.email,
            constituency=voter_data.constituency,
            face_embeddings_path=voter_data.face_embeddings_path,
            face_image_path=voter_data.face_image_path,
            verification_status="PENDING",
            has_voted=False,
            created_by=admin_id,
            created_at=datetime.now()
        )

        return VoterRepository.create_voter(
            db,
            voter
        )

    @staticmethod
    def get_all_voters(db: Session):

        return VoterRepository.get_all_voters(db)

    @staticmethod
    def get_voter(
        db: Session,
        voter_id: int
    ):

        voter = VoterRepository.get_voter_by_id(
            db,
            voter_id
        )

        if not voter:
            raise ValueError(
                "Voter not found."
            )

        return voter

    @staticmethod
    def update_voter(
        db: Session,
        voter_id: int,
        voter_data: VoterUpdate
    ):

        voter = VoterRepository.get_voter_by_id(
            db,
            voter_id
        )

        if not voter:
            raise ValueError(
                "Voter not found."
            )

        # Check duplicate email
        if voter_data.email:
            existing_voter = VoterRepository.get_voter_by_email(
                db,
                voter_data.email
            )

            if existing_voter and existing_voter.voter_id != voter_id:
                raise ValueError(
                    "A voter with this email already exists."
                )

        # Check duplicate phone
        existing_voter = VoterRepository.get_voter_by_phone(
            db,
            voter_data.phone
        )

        if existing_voter and existing_voter.voter_id != voter_id:
            raise ValueError(
                "A voter with this phone number already exists."
            )

        voter.full_name = voter_data.full_name
        voter.father_name = voter_data.father_name
        voter.dob = voter_data.dob
        voter.gender = voter_data.gender
        voter.phone = voter_data.phone
        voter.email = voter_data.email
        voter.constituency = voter_data.constituency
        voter.face_embeddings_path = voter_data.face_embeddings_path
        voter.face_image_path = voter_data.face_image_path

        return VoterRepository.update_voter(
            db,
            voter
        )

    @staticmethod
    def delete_voter(
        db: Session,
        voter_id: int
    ):

        voter = VoterRepository.get_voter_by_id(
            db,
            voter_id
        )

        if not voter:
            raise ValueError(
                "Voter not found."
            )

        VoterRepository.delete_voter(
            db,
            voter
        )

        return {
            "message": "Voter deleted successfully."
        }