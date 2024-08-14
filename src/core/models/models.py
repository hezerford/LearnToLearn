from sqlalchemy import ForeignKey, String, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column

from src.core.models.mixins.int_id_pk import IntIdPkMixin

from .base import Base

class User(IntIdPkMixin, Base):
    username: Mapped[str] = mapped_column(unique=True)

    progress: Mapped[list["UserProgress"]] = relationship("UserProgress", back_populates="user")

class Translation(IntIdPkMixin, Base):
    english_word: Mapped[str] = mapped_column(String, index=True)
    russian_word: Mapped[str] = mapped_column(String)

    progress: Mapped[list["UserProgress"]] = relationship("UserProgress", back_populates="translation")

class UserProgress(IntIdPkMixin, Base):
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)
    translation_id: Mapped[int] = mapped_column(ForeignKey("translation.id"), primary_key=True)
    is_learned: Mapped[bool] = mapped_column(Boolean, default=False)

    user: Mapped["User"] = relationship("User", back_populates="progress")
    translation: Mapped["Translation"] = relationship("Translation", back_populates="progress")


# class User(Base):
#     __tablename__ = "users" 

#     username = Column(String, unique=True, index=True)

#     progress = relationship("UserProgress", back_populates="user")

# class Translations(Base):
#     __tablename__ = "translations"

#     id = Column(Integer, primary_key=True, index=True)
#     english_word = Column(String, index=True)
#     russian_word = Column(String)

#     progress = relationship("UserProgress", back_populates="translation")

# class UserProgress(Base):
#     __tablename__ = "user_progress"

#     user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
#     translation_id = Column(Integer, ForeignKey("translations.id"), primary_key=True)
#     is_learned = Column(Boolean, default=False)

#     user = relationship("User", back_populates="progress") # для работы 25 строки
#     translation = relationship("Translations", back_populates="progress") # для работы 26 строки