from app.database.crud import CRUDBase
from app.database.models import Users
from app.models.users import UserSchema


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

    def update_user(self, user_id: int, **kwargs) -> UserSchema:
        user = self.get(id=user_id)
        updated_user = self.update(user, **kwargs)
        return UserSchema.model_validate(updated_user)

    def delete_user(self, user_id: int) -> None:
        user = self.get(id=user_id)
        self.delete(user)
