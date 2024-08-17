from typing import TYPE_CHECKING, Annotated

from fastapi import Depends

from src import database
from src.core.auth.models import User

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

async def get_users_db(session: Annotated["AsyncSession", Depends(database.session_getter)]):
    yield User.get_db(session=session)