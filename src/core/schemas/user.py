import uuid

from fastapi_users import schemas

from src.utils.user_id import UserIdType


class UserRead(UserIdType):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass