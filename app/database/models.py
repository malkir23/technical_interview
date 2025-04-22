from sqlalchemy import ForeignKey
from app.database.database import Base, UniqueMixin
from sqlalchemy.orm import Mapped, mapped_column


class Users(Base):
    name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    is_active: Mapped[bool] = mapped_column(default=False)
    group_id: Mapped[int] = mapped_column(ForeignKey('usergroups.id'))

class UserGroups(Base):
    group_name: Mapped[str] = UniqueMixin.uniq_str()
    group_description: Mapped[str]
