from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import require_patient
from app.db.session import get_db
from app.db.models import Appointment

router = APIRouter(prefix="/appointments", tags=["Appointments"])

@router.post("")
def book_appointment(
    doctor_id: int,
    start_time: str,
    end_time: str,
    patient=Depends(require_patient),
    db: Session = Depends(get_db),
):
    conflict = db.query(Appointment).filter(
        Appointment.doctor_id == doctor_id,
        Appointment.start_time < end_time,
        Appointment.end_time > start_time
    ).first()

    if conflict:
        raise HTTPException(status_code=400, detail="Slot already booked")

    appt = Appointment(
        doctor_id=doctor_id,
        patient_id=patient.id,
        start_time=start_time,
        end_time=end_time
    )
    db.add(appt)
    db.commit()
    return appt

@router.delete("/{appointment_id}")
def cancel_appointment(
    appointment_id: int,
    patient=Depends(require_patient),
    db: Session = Depends(get_db),
):
    appt = db.query(Appointment).get(appointment_id)
    if not appt or appt.patient_id != patient.id:
        raise HTTPException(status_code=403)
    db.delete(appt)
    db.commit()
    return {"message": "Cancelled"}
