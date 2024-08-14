from contextlib import asynccontextmanager
from src.database import db_helper
from fastapi.responses import ORJSONResponse
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    await db_helper.dispose()

def create_app() -> FastAPI:
    app = FastAPI(
        default_response_class=ORJSONResponse,
        lifespan=lifespan,
    )
    return app