from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.core.jwt import decode_token
from app.db.session import get_db
from app.db.models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    payload = decode_token(token)
    user = db.query(User).get(int(payload["sub"]))
    if not user:
        raise HTTPException(status_code=401)
    return user

def require_doctor(user: User = Depends(get_current_user)):
    if user.role != "doctor":
        raise HTTPException(status_code=403)
    return user

def require_patient(user: User = Depends(get_current_user)):
    if user.role != "patient":
        raise HTTPException(status_code=403)
    return user
