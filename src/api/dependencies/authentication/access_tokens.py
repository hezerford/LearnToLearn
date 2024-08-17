from typing import TYPE_CHECKING, Annotated

from fastapi import Depends

from src.core.auth.models import AccessToken
from src import database
from src.core.auth.models import User

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

async def get_access_tokens_db(session: Annotated["AsyncSession", Depends(database.session_getter)]):  
    yield AccessToken.get_db(session=session)