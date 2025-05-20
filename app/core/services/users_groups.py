from app.database.database import get_session
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from app.repositories.users_groups_repository import UserGroupRepository

def get_users_groups_repository(
    session: Session = Depends(get_session)
) -> UserGroupRepository:
    return UserGroupRepository(session)


def check_existing_user_group(
    group_id: int,
    users_groups_repo: UserGroupRepository = Depends(get_users_groups_repository)
) -> UserGroupRepository:
    existing_user_group = users_groups_repo.get_group(id=group_id)

    if existing_user_group:
        raise HTTPException(status_code=400, detail="User group already exists")
    return users_groups_repo
