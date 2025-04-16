from wsgiref.validate import validator
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserSchema(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool = True
    created_at: datetime
    updated_at: Optional[datetime] = None

    @validator('email')
    def validate_email(self, value):
        if not value.endswith('.com'):
            raise ValueError


    class Config:
        orm_mode = True
