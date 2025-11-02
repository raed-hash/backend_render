from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import get_db
from ..models import Owner, User
from ..schemas import OwnerValidateIn, OwnerValidateOut, LoginIn, LoginOut
from ..core.security import verify_password, create_jwt

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/validate-owner", response_model=OwnerValidateOut)
def validate_owner(payload: OwnerValidateIn, db: Session = Depends(get_db)):
    slug = payload.owner_id.strip().lower()
    if len(slug) < 2:
        raise HTTPException(status_code=400, detail="owner_id inválido")
    owner = db.query(Owner).filter(Owner.slug == slug).first()
    if not owner:
        raise HTTPException(status_code=404, detail="owner não encontrado")
    return OwnerValidateOut(ok=True)

@router.post("/login", response_model=LoginOut)
def login(payload: LoginIn, db: Session = Depends(get_db)):
    slug = payload.owner_id.strip().lower()
    owner = db.query(Owner).filter(Owner.slug == slug).first()
    if not owner:
        raise HTTPException(status_code=404, detail="owner não encontrado")
    user = db.query(User).filter(User.owner_id == owner.id, User.email == payload.email.lower()).first()
    if not user or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    token = create_jwt(str(user.id))
    return LoginOut(ok=True, token=token)
