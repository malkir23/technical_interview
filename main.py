from database import create_tables, get_db
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
from database.models import PlayingWithNeon

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/tests")
def read_tests(db: Session = Depends(get_db)):
    tests = db.query(PlayingWithNeon).all()
    return tests

@app.on_event("startup")
def startup_event():
    create_tables()
