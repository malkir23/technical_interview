from fastapi import APIRouter
from app.repositories.user_repository import UserRepository
from app.models.users import UserSchema, UserCreate, UserUpdate
from fastapi import Depends
from app.core.services.users import get_user_repository, check_existing_user
from fastapi import HTTPException, status


router = APIRouter()


@router.get("/", response_model=list[UserSchema])
async def list_users(
    user_repo: UserRepository = Depends(get_user_repository),
) -> list[UserSchema]:
    users = user_repo.get_all_users()
    return users


@router.post("/", response_model=UserCreate, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_data: UserCreate,
    user_repo: UserRepository = Depends(check_existing_user),
) -> UserCreate:
    try:
        user = user_repo.create_user(user_data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e) from e
    return user


@router.patch("/{user_id}", response_model=UserUpdate)
async def update_user(
    user_id: int,
    user_update_data: UserUpdate,
    user_repo: UserRepository = Depends(get_user_repository),
) -> UserUpdate:
    try:
        user = user_repo.update_user({"id": user_id}, user_update_data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e) from e
    return user


@router.delete("/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(
    user_id: int, user_repo: UserRepository = Depends(get_user_repository)
) -> None:
    try:
        user_repo.delete_user(user_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Can`t delete user"
        ) from e
