from typing import TYPE_CHECKING, Annotated

from fastapi import Depends

from src.core.models import AccessToken, database

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

async def get_access_tokens_db(
    session: Annotated[
        "AsyncSession",
        Depends(database.DatabaseHelper.session_getter),
    ],
):
    yield AccessToken.get_db(session=session)