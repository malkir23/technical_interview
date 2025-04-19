from sqlalchemy.sql import func
from sqlalchemy import (
    Column, Integer, String, Boolean, DateTime, ForeignKey, Float
)
from app.database.database import Base

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True, nullable=True)
    is_active = Column(Boolean, default=True)
    create_time = Column(DateTime(timezone=True), server_default=func.now())
    update_time = Column(DateTime(timezone=True), onupdate=func.now())
    group_id = Column(Integer, ForeignKey('user_groups.id'))

class UserGroups(Base):
    __tablename__ = 'user_groups'

    id = Column(Integer, primary_key=True)
    group_name = Column(String, unique=True)

