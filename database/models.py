from sqlalchemy.sql import func
from sqlalchemy import (
	Column, Integer, String, Boolean, Datetime, ForeignKey, List, Float
)
from database import Base


class Users(Base):
    __table_name__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True, nullabel=True)
    is_active = Column(Boolean, default=True)
    create_time = Column(Datetime(timezone=True), server_default=func.now())
    update_time = Column(Datetime(timezone=True), onupdate=func.now())
    group = Column(List, ForeignKey('user_groups.id'))


class UserGroups(Base):
    __name__ = 'user groups'

    id = Column(Integer, primary_key=True)
    group_name = Column(String, unique=True)


class PlayingWithNeon(Base):
    __tablename__ = 'playing_with_neon'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    value = Column(Float)
