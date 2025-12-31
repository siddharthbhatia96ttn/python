from sqlalchemy import Column, Integer, String
from app.database import Base   # ✅ THIS LINE WAS MISSING

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, index=True)
    password_hash = Column(String(100))
    role = Column(String(100))
    name = Column(String(100))
