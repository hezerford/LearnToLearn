from typing import TYPE_CHECKING, Annotated

from fastapi import Depends

from src.core.models import database
from src.core.models import User

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

async def get_users_db(session: Annotated["AsyncSession", Depends(database.DatabaseHelper.session_getter)]):
    yield User.get_db(session=session)