from pydantic import BaseModel, EmailStr

class OwnerValidateIn(BaseModel):
    owner_id: str

class OwnerValidateOut(BaseModel):
    ok: bool

class LoginIn(BaseModel):
    owner_id: str
    email: EmailStr
    password: str

class LoginOut(BaseModel):
    ok: bool
    token: str | None = None
