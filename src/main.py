from contextlib import asynccontextmanager
import logging
from fastapi import FastAPI

import uvicorn

from config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info(f"Info DB: {settings.db.url}")

from src.database import db_helper

from api import router as api_router

@asynccontextmanager
async def lifespan():
    # startup
    yield
    # shutdown
    await db_helper.dispose()

main_app = FastAPI(
    lifespan=lifespan,
)

main_app.include_router(api_router, prefix=settings.api.prefix)

if __name__ == "__main__":
    uvicorn.run("main:main_app", 
                host=settings.run.host,
                port=settings.run.port,
                reload=True)