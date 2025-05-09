from fastapi import APIRouter
from app.repositories.user_repository import UserRepository
from app.models.users import UserSchema, UserCreate, UserUpdate
from fastapi import Depends
from app.database.database import get_session
from sqlalchemy.orm import Session


router = APIRouter()

@router.get("/users", response_model=list[UserSchema])
def list_users(session: Session = Depends(get_session)) -> list[UserSchema]:
    users = UserRepository(session).get_all_users() or []
    return users

@router.post("/users", response_model=UserCreate)
def create_user(
    user: UserCreate, session: Session = Depends(get_session)
) -> UserCreate:
    user = UserRepository(session).create_user(**user.dict())
    return user

@router.patch("/users", response_model=UserUpdate)
def update_user(
    user: UserUpdate, session: Session = Depends(get_session)
) -> UserUpdate:
    user = UserRepository(session).update_user(**user.dict())
    return user
