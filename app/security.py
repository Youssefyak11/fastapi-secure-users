from passlib.context import CryptContext

# bcrypt_sha256 avoids bcrypt's 72-byte password limit by hashing first with SHA-256
_pwd = CryptContext(schemes=["bcrypt_sha256"], deprecated="auto")

def hash_password(plain: str) -> str:
    return _pwd.hash(plain)

def verify_password(plain: str, hashed: str) -> bool:
    return _pwd.verify(plain, hashed)
