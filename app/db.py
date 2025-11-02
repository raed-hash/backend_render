from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .core.config import settings

engine = create_engine(settings.PG_DSN, pool_pre_ping=True) if settings.PG_DSN else None
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) if engine else None

def get_db():
    if SessionLocal is None:
        raise RuntimeError("DB não configurado: defina PG_DSN nas variáveis de ambiente")
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
