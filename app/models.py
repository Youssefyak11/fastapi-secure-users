from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import validates
from .db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    @validates("email")
    def validate_email(self, key, value: str):
        if "@" not in value or "." not in value.split("@")[-1]:
            raise ValueError("Invalid email")
        return value
