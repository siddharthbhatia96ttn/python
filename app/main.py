from fastapi import FastAPI
from app.database import engine, Base

# IMPORTANT: import classes, not files
from app.models import User, Availability, Appointment

app = FastAPI()

@app.on_event("startup")
def create_tables():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Doctor Appointment API with MySQL"}
