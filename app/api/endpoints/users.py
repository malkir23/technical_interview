from fastapi import Depends, APIRouter

from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.models.users import UserSchema
from app.database.database import get_session

router = APIRouter()

@router.get("/users", response_model=list[UserSchema])
def list_users(session: Session = Depends(get_session)) -> list[UserSchema]:
    users = UserRepository(session).get_all_users()
    if not users:
        users = []
    return users

@router.post("/users", response_model=UserSchema)
def create_user(user: UserSchema, session: Session = Depends(get_session)) -> UserSchema:
    user = UserRepository(session).create_user(**user.dict())
    return user
