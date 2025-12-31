from sqlalchemy.orm import Session
from app.db.models import Appointment

def book_appointment(db: Session, doctor_id, patient_id, start, end):
    conflict = db.query(Appointment).filter(
        Appointment.doctor_id == doctor_id,
        Appointment.start_time < end,
        Appointment.end_time > start
    ).first()

    if conflict:
        raise ValueError("Slot already booked")

    appointment = Appointment(
        doctor_id=doctor_id,
        patient_id=patient_id,
        start_time=start,
        end_time=end
    )
    db.add(appointment)
    db.commit()
    db.refresh(appointment)
    return appointment
