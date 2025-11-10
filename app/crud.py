from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from . import models, security, schemas

def create_user(db: Session, data: schemas.UserCreate) -> models.User:
    user = models.User(
        username=data.username,
        email=data.email,
        password_hash=security.hash_password(data.password),
    )
    db.add(user)
    try:
        db.commit()
    except IntegrityError as e:
        db.rollback()
        raise ValueError("Username or email already exists") from e
    db.refresh(user)
    return user

def get_user_by_username(db: Session, username: str) -> models.User | None:
    return db.query(models.User).filter(models.User.username == username).one_or_none()
