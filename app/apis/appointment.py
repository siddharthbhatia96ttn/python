from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import require_patient
from app.services.appointment_service import book_appointment
from app.db.session import get_db

router = APIRouter(prefix="/appointments", tags=["Appointments"])

@router.post("")
def book(
    doctor_id: int,
    start_time: str,
    end_time: str,
    patient=Depends(require_patient),
    db: Session = Depends(get_db)
):
    try:
        return book_appointment(
            db, doctor_id, patient.id, start_time, end_time
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
