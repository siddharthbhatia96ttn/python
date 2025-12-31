from sqlalchemy.orm import Session
from app.core.security import hash_password, verify_password
from app.core.jwt import create_access_token
from app.db.models import User

def register_user(db: Session, data):
    user = User(
        email=data.email,
        name=data.name,
        role=data.role,
        password_hash=hash_password(data.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.password_hash):
        return None
    return user

def login_user(user: User):
    token = create_access_token({
        "sub": str(user.id),
        "role": user.role
    })
    return token
