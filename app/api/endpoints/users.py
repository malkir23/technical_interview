from fastapi import Depends, APIRouter

from sqlalchemy.orm import Session
from app.database.models import Users
from app.database.database import get_db

router = APIRouter()

@router.get("/users", response_model=list[Users])
def list_users(db: Session = Depends(get_db)) -> list[Users]:
    users = db.query(Users).all()
    return users
