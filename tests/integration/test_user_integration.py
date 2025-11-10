import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db import Base
from app.schemas import UserCreate
from app.crud import create_user

TEST_DB_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql+psycopg://postgres:postgres@localhost:5432/testdb",
)

@pytest.fixture(scope="session")
def db_engine():
    engine = create_engine(TEST_DB_URL, future=True)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield engine
    Base.metadata.drop_all(bind=engine)

@pytest.fixture()
def db(db_engine):
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine, future=True)
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()

def test_create_user_and_uniqueness(db):
    u = create_user(db, UserCreate(username="alice", email="alice@example.com", password="abcdef"))
    assert u.id is not None
    with pytest.raises(ValueError):
        create_user(db, UserCreate(username="alice", email="alice2@example.com", password="abcdef"))
    with pytest.raises(ValueError):
        create_user(db, UserCreate(username="alice2", email="alice@example.com", password="abcdef"))

def test_invalid_email_db_level(db):
    with pytest.raises(ValueError):
        create_user(db, UserCreate(username="bademail", email="noatsign", password="abcdef"))
