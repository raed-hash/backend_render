from datetime import datetime, timedelta, timezone
from jose import jwt
from passlib.context import CryptContext
from .config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(raw: str) -> str:
    return pwd_context.hash(raw)

def verify_password(raw: str, hashed: str) -> bool:
    return pwd_context.verify(raw, hashed)

def create_jwt(sub: str) -> str:
    now = datetime.now(tz=timezone.utc)
    exp = now + timedelta(minutes=settings.JWT_EXPIRES_MIN)
    payload = {"sub": sub, "iat": int(now.timestamp()), "exp": int(exp.timestamp())}
    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALG)
