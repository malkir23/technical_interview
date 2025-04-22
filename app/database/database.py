from datetime import datetime
from typing import Annotated

from sqlalchemy import create_engine, func
from sqlalchemy.orm import (
	DeclarativeBase, declared_attr, Mapped, mapped_column, sessionmaker
)
from sqlalchemy.ext.asyncio import AsyncAttrs
from app.core.config import settings


engine = create_engine(settings.PG_DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    create_at: Mapped[datetime] = mapped_column(server_default=func.now())
    update_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), onupdate=func.now()
    )

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

class UniqueMixin:

    @staticmethod
    def uniq_str():
        return Annotated[str, mapped_column(unique=True)]

def create_tables():
    Base.metadata.create_all(bind=engine)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
