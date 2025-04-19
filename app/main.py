from app.database.database import create_tables

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(site.route, tags=["Site"])

@app.on_event("startup")
def startup_event():
    create_tables()
