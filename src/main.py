import uvicorn

from src.create_fastapi_app import create_app
from src.core.config import settings

from src.api import router as api_router

main_app = create_app()

main_app.include_router(api_router, prefix=settings.api.prefix)

if __name__ == "__main__":
    uvicorn.run("src.main:main_app", 
                host=settings.run.host,
                port=settings.run.port,
                reload=True)