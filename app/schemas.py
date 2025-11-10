from pydantic import BaseModel, EmailStr, constr

class UserCreate(BaseModel):
    username: constr(strip_whitespace=True, min_length=3, max_length=50)
    email: EmailStr
    password: constr(min_length=6, max_length=128)

class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True
