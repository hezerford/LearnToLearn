from contextlib import asynccontextmanager
from fastapi import FastAPI

from fastapi.responses import ORJSONResponse
import uvicorn

from src.core.config import settings

from src.database import db_helper

from src.api import router as api_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    await db_helper.dispose()

main_app = FastAPI(
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)

main_app.include_router(api_router, prefix=settings.api.prefix)

if __name__ == "__main__":
    uvicorn.run("src.main:main_app", 
                host=settings.run.host,
                port=settings.run.port,
                reload=True)