from sys import prefix
from fastapi import FastAPI
from app.database.database import create_tables
from app.api.endpoints import users, user_group
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(
    user_group.router, prefix="/user_group", tags=["User Ggroup"]
)
