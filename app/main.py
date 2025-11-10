from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .db import Base, engine, get_db
from . import schemas, crud

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Secure Users API")

@app.post("/users", response_model=schemas.UserRead, status_code=status.HTTP_201_CREATED)
def create_user(payload: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        user = crud.create_user(db, payload)
        return user
    except ValueError:
        raise HTTPException(status_code=400, detail="Username or email already exists")

@app.get("/users/{username}", response_model=schemas.UserRead)
def read_user(username: str, db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
