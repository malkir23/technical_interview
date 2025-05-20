from app.database.crud import CRUDBase
from app.database.models import UserGroups
from app.models.users_groups import UserGroupGetSchema, UserGroupSchema


class UserGroupRepository(CRUDBase):
    def __init__(self, session):
        super().__init__(session=session, model=UserGroups)

    def create_group(self, user_data) -> UserGroupSchema:
        group = self.create(user_data.dict())
        return UserGroupSchema.model_validate(group)

    def get_group(self, **kwargs) -> UserGroupGetSchema:
        group = self.get(**kwargs)
        return UserGroupGetSchema.model_validate(group)

    def get_all_groups(self) -> list[UserGroupGetSchema]:
        groups = self.get_all()
        return [UserGroupGetSchema.model_validate(group) for group in groups]

    def update_group(self, get_filter: dict, group_update_data: UserGroupSchema) -> UserGroupSchema:
        updated_group = self.update(
            get_filter, group_update_data.model_dump(exclude_unset=True)
        )
        return UserGroupSchema.model_validate(updated_group)

    def delete_group(self, user_id: int) -> None:
        self.delete(user_id)
