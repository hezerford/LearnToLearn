from typing import TYPE_CHECKING
from fastapi_users.db import SQLAlchemyBaseUserTable
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.orm import Mapped, mapped_column

from src.core.models import Base
from src.core.models.mixins.int_id_pk import IntIdPkMixin
from src.utils.user_id import UserIdType

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

class User(Base, IntIdPkMixin, SQLAlchemyBaseUserTable[UserIdType]):
    username: Mapped[str] = mapped_column(unique=True)

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, User)