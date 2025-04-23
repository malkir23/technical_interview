from fastapi import APIRouter
from app.repositories.user_repository import UserRepository
from app.models.users import UserSchema, UserCreate, UserUpdate


router = APIRouter()

@router.get("/users", response_model=list[UserSchema])
def list_users() -> list[UserSchema]:
    users = UserRepository().get_all_users() or []
    return users

@router.post("/users", response_model=UserCreate)
def create_user(user: UserCreate) -> UserCreate:
    user = UserRepository().create_user(**user.dict())
    return user
