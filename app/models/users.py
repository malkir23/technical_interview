from pydantic import BaseModel, validator, Field
from typing import Optional

class EmailBase(BaseModel):
    email: str = Field(min_length=5, max_length=50)
    @validator('email')
    def validate_email(cls, value):
        if not value.endswith('.com'):
            raise ValueError("Email must end with '.com'")
        return value

class UserCreate(EmailBase):
    name: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=8, max_length=40)
    group_id: Optional[int] = None

class UserUpdate(EmailBase):
    name: Optional[str] = Field(min_length=3, max_length=50)
    password: Optional[str] = Field(min_length=8, max_length=40)
    group_id: Optional[int] = None


class UserSchema(EmailBase):
    id: int
    name: str
    password: str
    is_active: bool = True
    group_id: Optional[int] = None

    class Config:
        from_attributes = True
