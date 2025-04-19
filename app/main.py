from fastapi import FastAPI
from app.database.database import create_tables
from app.api.endpoints import users

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(users.router, tags=["Users"])

@app.on_event("startup")
def startup_event():
    create_tables()
