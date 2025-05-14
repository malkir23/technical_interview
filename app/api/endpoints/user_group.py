from fastapi import APIRouter
from app.repositories.user_repository import UserRepository
from app.models.users_groups import UserGroupSchema
from fastapi import Depends
from app.core.services.users_groups import get_users_groups_repository
from fastapi import HTTPException, status


router = APIRouter()


@router.get("/", response_model=list[UserGroupSchema])
async def list_users_groups(
    users_groups_repo: UserRepository = Depends(get_users_groups_repository),
) -> list[UserGroupSchema]:
    users_groups = users_groups_repo.get_all_users()
    return users_groups

@router.get("/{group_id}", response_model=UserGroupSchema)
async def get_user_group(
    group_id: int,
    users_groups_repo: UserRepository = Depends(get_users_groups_repository),
) -> UserGroupSchema:
    user_group = users_groups_repo.get_user_group(id=group_id)
    if not user_group:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User group not found")
    return user_group


# @router.post("/", response_model=UserCreate, status_code=status.HTTP_201_CREATED)
# async def create_user(
#     user_data: UserCreate,
#     user_repo: UserRepository = Depends(check_existing_user),
# ) -> UserCreate:
#     try:
#         user = user_repo.create_user(user_data)
#     except Exception as e:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e) from e
#     return user

# @router.get("/{user_id}", response_model=UserSchema)
# async def get_user(
#     user_id: int,
#     user_repo: UserRepository = Depends(get_user_repository),
# ) -> UserSchema:
#     users = user_repo.get_user(id=user_id)
#     return users



# @router.patch("/{user_id}", response_model=UserUpdate)
# async def update_user(
#     user_id: int,
#     user_update_data: UserUpdate,
#     user_repo: UserRepository = Depends(get_user_repository),
# ) -> UserUpdate:
#     try:
#         user = user_repo.update_user({"id": user_id}, user_update_data)
#     except Exception as e:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e) from e
#     return user


# @router.delete("/{user_id}", status_code=status.HTTP_200_OK)
# async def delete_user(
#     user_id: int, user_repo: UserRepository = Depends(get_user_repository)
# ) -> None:
#     try:
#         user_repo.delete_user(user_id)
#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST, detail="Can`t delete user"
#         ) from e
