from fastapi import APIRouter, Depends, HTTPException, status

from app.core.services.users_groups import (
	get_users_groups_repository, check_existing_user_group

)
from app.models.users_groups import UserGroupSchema, UserGroupGetSchema
from app.repositories.users_groups_repository import UserGroupRepository

router = APIRouter()


@router.get(
    "/",
    response_model=list[UserGroupGetSchema],
    status_code=status.HTTP_200_OK
)
def list_users_groups(
    users_groups_repo: UserGroupRepository = Depends(get_users_groups_repository)
) -> list[UserGroupGetSchema]:
    return users_groups_repo.get_all_groups()


@router.get(
    "/{group_id}",
    response_model=UserGroupGetSchema,
    status_code=status.HTTP_200_OK
)
def get_user_group(
    group_id: int,
    users_groups_repo: UserGroupRepository = Depends(get_users_groups_repository)
) -> UserGroupGetSchema:
    user_group = users_groups_repo.get_group(id=group_id)
    if not user_group:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User group not found"
        )
    return user_group


@router.post(
    '/',
    response_model=UserGroupSchema,
    status_code=status.HTTP_201_CREATED
)
def create_user_group(
    user_group_data: UserGroupSchema,
    users_groups_repo: UserGroupRepository = Depends(get_users_groups_repository)
) -> UserGroupSchema:
    try:
        user_group = users_groups_repo.create_group(user_group_data)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=e
        ) from e
    return user_group

@router.patch(
    "/{group_id}",
    response_model=UserGroupSchema,
    status_code=status.HTTP_200_OK
)
def update_user_group(
    group_id: int,
    user_group_data: UserGroupSchema,
    users_groups_repo: UserGroupRepository = Depends(get_users_groups_repository)
) -> UserGroupSchema:
    try:
        user_group = users_groups_repo.update_group(
            {"id": group_id}, user_group_data
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=e
        ) from e
    return user_group

@router.delete("/{group_id}", status_code=status.HTTP_200_OK)
def delete_user_group(
    group_id: int,
    users_groups_repo: UserGroupRepository = Depends(get_users_groups_repository),
) -> None:
    try:
        users_groups_repo.delete_group(group_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Can't delete user group"
        ) from e
    return None
