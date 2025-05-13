from app.database.database import get_session
from sqlalchemy.orm import Session
from fastapi import Depends
from app.repositories.user_repository import UserRepository
from app.core.exceptions.user import UserAlreadyExists, UsersNotFound

def get_user_repository(session: Session = Depends(get_session)) -> UserRepository:
    return UserRepository(session)


def check_existing_user(
    user_id: int,
    user_repo: UserRepository = Depends(get_user_repository)
) -> UserRepository:
    existing_user = user_repo.get_user(user_id)

    if existing_user:
        raise UserAlreadyExists(user_id)
    return user_repo
