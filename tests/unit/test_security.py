from app.security import hash_password, verify_password

def test_password_hash_and_verify():
    raw = "supersecret"
    hashed = hash_password(raw)
    assert hashed != raw
    assert verify_password(raw, hashed) is True
    assert verify_password("wrong", hashed) is False
