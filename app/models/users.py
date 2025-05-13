from pydantic import BaseModel, ValidationInfo, field_validator, Field
from typing import Optional

class EmailBase(BaseModel):
    email: str = Field(min_length=5, max_length=50)
    @field_validator('email')
    def validate_email(cls, value: str, info: ValidationInfo) -> str:
        if not value.endswith('.com'):
            raise ValueError("Email must end with '.com'")
        return value

class UserCreate(EmailBase):
    name: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=8, max_length=40)
    group_id: Optional[int] = None

class UserUpdate(EmailBase):
    name: Optional[str] = Field(None, min_length=3, max_length=50)
    password: Optional[str] = Field(None, min_length=8, max_length=40)
    email: Optional[str] = Field(None, min_length=5, max_length=50)
    group_id: Optional[int] = None
    is_active: Optional[bool] = None
    class Config:
        from_attributes = True


class UserSchema(EmailBase):
    id: int
    name: str
    password: str
    is_active: bool = True
    group_id: Optional[int] = None

    class Config:
        from_attributes = True
