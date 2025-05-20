from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.endpoints import user_group, users
from app.database.database import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    create_tables()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root() -> dict:
    """Root endpoint that returns a welcome message.

    Returns:
        dict: A dictionary containing a welcome message.

    """
    return {"message": "Welcome to the FastAPI application!"}


app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(
    user_group.router, prefix="/user_group", tags=["User Group"]
)
