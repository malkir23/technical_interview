from pydantic import BaseModel, validator, Field
from datetime import datetime
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
    is_active: bool = True

class UserUpdate(EmailBase):
    name: Optional[str] = Field(min_length=3, max_length=50)
    password: Optional[str] = Field(min_length=8, max_length=40)
    group_id: Optional[int] = None
    is_active: Optional[bool] = None


class UserSchema(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at: datetime
    updated_at: Optional[datetime] = None
    group_id: Optional[int] = None

    class Config:
        from_attributes = True
