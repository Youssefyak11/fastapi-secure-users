import pytest
from pydantic import ValidationError
from app.schemas import UserCreate

def test_usercreate_valid():
    u = UserCreate(username="alice", email="alice@example.com", password="123456")
    assert u.username == "alice"

def test_usercreate_invalid_email():
    with pytest.raises(ValidationError):
        UserCreate(username="bob", email="not-an-email", password="123456")
