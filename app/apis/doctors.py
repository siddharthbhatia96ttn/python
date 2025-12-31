from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import require_doctor
from app.db.session import get_db
from app.db.models import Availability

router = APIRouter(prefix="/doctors", tags=["Doctors"])

@router.post("/availability")
def set_availability(
    start_time: str,
    end_time: str,
    doctor=Depends(require_doctor),
    db: Session = Depends(get_db)
):
    slot = Availability(
        doctor_id=doctor.id,
        start_time=start_time,
        end_time=end_time
    )
    db.add(slot)
    db.commit()
    return slot

@router.get("/{doctor_id}/availability")
def get_availability(doctor_id: int, db: Session = Depends(get_db)):
    return db.query(Availability).filter(
        Availability.doctor_id == doctor_id
    ).all()
