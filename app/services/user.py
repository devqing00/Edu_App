from app.models.user import User
from sqlalchemy.orm import Session
from uuid import UUID

from app.schemas.user import UserCreate
from app.core.security import get_password_hash

class UserService:

    @staticmethod
    def get_user_by_email(db_session: Session, email: str):
        return db_session.query(User).filter(User.email == email).first()
    
    @staticmethod
    def create_user(db_session: Session, user_data: UserCreate):
        new_user = User(
            email=user_data.email,
            hashed_password=get_password_hash(user_data.password),
            name=user_data.name,
            is_active=True,
            role = user_data.role

        )
        db_session.add(new_user)
        db_session.flush()
        db_session.refresh(new_user)
        return new_user