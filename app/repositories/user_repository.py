from app.database.crud import CRUDBase
from app.database.models import Users
from app.models.users import UserSchema


class UserRepository(CRUDBase):
    def __init__(self, session):
        super().__init__(session)

    def create_user(self, **kwargs) -> UserSchema:
        user = self.create(Users, **kwargs)
        return UserSchema.from_orm(user)

    def get_user(self, user_id: int) -> UserSchema:
        user = self.read(Users, id=user_id)
        return UserSchema.from_orm(user)

    def update_user(self, user_id: int, **kwargs) -> UserSchema:
        user = self.read(Users, id=user_id)
        updated_user = self.update(user, **kwargs)
        return UserSchema.from_orm(updated_user)

    def delete_user(self, user_id: int) -> None:
        user = self.read(Users, id=user_id)
        self.delete(user)
