from fastapi import Depends, APIRouter

from sqlalchemy.orm import Session
from app.database.models import Users
from app.models.users import UserSchema
from app.database.database import get_db

router = APIRouter()
@router.get("/users", response_model=list[UserSchema])
def list_users(db: Session = Depends(get_db)) -> list[UserSchema]:
    users = db.query(Users).all()
    return [UserSchema.from_orm(user) for user in users]
