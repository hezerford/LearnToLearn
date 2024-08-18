from fastapi import APIRouter

from .fastapi_users import fastapi_users
from src.api.dependencies.authentication.backend import authentication_backend
from src.core.config import settings

router = APIRouter(
    prefix=settings.api.v1.auth,
    tags=["Auth"],
)

# /login
# /logout
router.include_router(
    router=fastapi_users.get_auth_router(
        authentication_backend,
    ),
)

# /register
router.include_router(
    router=fastapi_users.get_register_router(
        UserRead,
        UserCreate,
    ),
)
