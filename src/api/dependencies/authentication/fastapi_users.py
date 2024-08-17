from fastapi_users import FastAPIUsers

from src.core.auth.models import User
from src.utils.user_id import UserIdType

from .user_manager import get_user_manager
from .backend import authentication_backend

fastapi_users = FastAPIUsers[User, UserIdType](
    get_user_manager,
    [authentication_backend],
)