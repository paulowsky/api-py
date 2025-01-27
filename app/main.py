from fastapi import FastAPI, Depends
from .config.env import settings
import uvicorn

from app.routers.v1 import user as user_v1


app = FastAPI()
app.include_router(user_v1.router, prefix="/v1", tags=["user"])


@app.get("/healthz")
async def healthz():
    return {"status": "OK"}


def start():
    """Launched with poetry run start at root level"""
    uvicorn.run("app.main:app", host=settings.host, port=settings.port, reload=settings.hot_reload_enabled)
