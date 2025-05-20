from pydantic import BaseModel
from typing import Optional

from app.models.users import UserSchema

class UserGroupSchema(BaseModel):
    group_name: str
    group_description: Optional[str] = ''

    class Config:
        from_attributes = True

class UserGroupGetSchema(BaseModel):
    id: int
    group_name: str
    group_description: Optional[str] = ''
    users: Optional[list[UserSchema]] = []

    class Config:
        from_attributes = True
