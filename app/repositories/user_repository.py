from app.database.crud import CRUDBase
from app.database.models import Users
from app.models.users import UserSchema, UserUpdate


class UserRepository(CRUDBase):
    def __init__(self, session):
        super().__init__(session=session, model=Users)

    def create_user(self, user_data) -> UserSchema:
        user = self.create(user_data.dict())
        return UserSchema.model_validate(user)

    def get_user(self, **kwargs) -> UserSchema:
        user = self.get(**kwargs)
        return UserSchema.model_validate(user)

    def get_all_users(self) -> list[UserSchema]:
        users = self.get_all()
        return [UserSchema.model_validate(user) for user in users]

    def update_user(self, get_filter: dict, user_update_data: UserUpdate) -> UserUpdate:
        updated_user = self.update(
            get_filter, user_update_data.model_dump(exclude_unset=True)
        )
        return UserUpdate.model_validate(updated_user)

    def delete_user(self, user_id: int) -> None:
        self.delete(user_id)
