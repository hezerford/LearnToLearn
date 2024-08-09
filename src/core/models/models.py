from sqlalchemy import MetaData, Column, ForeignKey, Integer, String, Boolean, Table
from sqlalchemy.orm import relationship, Mapped, mapped_column

from .base import Base

# metadata = MetaData()

# class User(Base):
#     __tablename__ = "users" 
    
#     username: Mapped[str] = mapped_column(unique=True)

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