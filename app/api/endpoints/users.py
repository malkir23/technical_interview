from fastapi import APIRouter
from app.repositories.user_repository import UserRepository
from app.models.users import UserSchema, UserCreate, UserUpdate
from fastapi import Depends
from app.database.database import get_session


router = APIRouter()

@router.get("/users", response_model=list[UserSchema])
def list_users(session: Depends(get_session)) -> list[UserSchema]:
    users = UserRepository(session).get_all_users() or []
    return users

@router.post("/users", response_model=UserCreate)
def create_user(user: UserCreate, session: Depends(get_session)) -> UserCreate:
    user = UserRepository(session).create_user(**user.dict())
    return user
