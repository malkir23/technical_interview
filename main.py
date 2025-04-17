from database import create_tables, get_db
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
from sqlachemy

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/tests")
def read_tests(db: Session = Depends(get_db)):

    playing_with_neon =

@app.on_event("startup")
def startup_event():
    create_tables()
