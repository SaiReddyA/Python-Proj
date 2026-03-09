from fastapi import FastAPI
from fastapi.params import Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base
import models
import schemas

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "Hello Sai"}


@app.post("/users")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)): # type: ignore
    new_user = models.User(name=user.name, age=user.age)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@app.get("/users")
def get_users(db: Session = Depends(get_db)): # type: ignore
    users = db.query(models.User).all()
    return users


@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)): # type: ignore
    user = db.query(models.User).filter(models.User.id == user_id).first()
    return user


@app.put("/users/{user_id}")
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)): # type: ignore

    db_user = db.query(models.User).filter(models.User.id == user_id).first()

    db_user.name = user.name # type: ignore
    db_user.age = user.age # type: ignore

    db.commit()
    db.refresh(db_user)

    return db_user


@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)): # type: ignore

    user = db.query(models.User).filter(models.User.id == user_id).first()

    db.delete(user)
    db.commit()

    return {"message": "User deleted"}