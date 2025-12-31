from sqlalchemy import Column, Integer, DateTime, ForeignKey
from app.database import Base   # ✅ REQUIRED

class Availability(Base):
    __tablename__ = "availabilities"

    id = Column(Integer, primary_key=True)
    doctor_id = Column(Integer, ForeignKey("users.id"))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
