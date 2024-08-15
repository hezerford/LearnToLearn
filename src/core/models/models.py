# from typing import TYPE_CHECKING
# from fastapi_users.db import SQLAlchemyBaseUserTable
# from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
# from sqlalchemy.orm import relationship, Mapped, mapped_column

# from .base import Base
# from src.core.models.mixins.int_id_pk import IntIdPkMixin

# if TYPE_CHECKING:
#     from sqlalchemy.ext.asyncio import AsyncSession

# class User(Base, IntIdPkMixin, SQLAlchemyBaseUserTable[int]):
#     username: Mapped[str] = mapped_column(unique=True)

#     @classmethod
#     def get_db(cls, session: "AsyncSession"):
#         return SQLAlchemyUserDatabase(session, User)

# class User(IntIdPkMixin, Base):
#     username: Mapped[str] = mapped_column(unique=True)

#     progress: Mapped[list["UserProgress"]] = relationship("UserProgress", back_populates="user")

# class Translation(IntIdPkMixin, Base):
#     english_word: Mapped[str] = mapped_column(String, index=True)
#     russian_word: Mapped[str] = mapped_column(String)

#     progress: Mapped[list["UserProgress"]] = relationship("UserProgress", back_populates="translation")

# class UserProgress(IntIdPkMixin, Base):
#     user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)
#     translation_id: Mapped[int] = mapped_column(ForeignKey("translation.id"), primary_key=True)
#     is_learned: Mapped[bool] = mapped_column(Boolean, default=False)

#     user: Mapped["User"] = relationship("User", back_populates="progress")
#     translation: Mapped["Translation"] = relationship("Translation", back_populates="progress")