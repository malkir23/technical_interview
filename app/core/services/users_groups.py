from app.database.database import get_session
from sqlalchemy.orm import Session
from fastapi import Depends
from app.repositories.users_groups_repository import UserGroupRepository

def get_users_groups_repository(session: Session = Depends(get_session)) -> UserGroupRepository:
    return UserGroupRepository(session)
