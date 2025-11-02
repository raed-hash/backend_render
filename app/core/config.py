import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PG_DSN = os.getenv("PG_DSN", "")
    JWT_SECRET = os.getenv("JWT_SECRET", "dev-secret-change")
    JWT_ALG = "HS256"
    JWT_EXPIRES_MIN = int(os.getenv("JWT_EXPIRES_MIN", "60"))
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*")

settings = Settings()
