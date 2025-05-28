from sqlalchemy.orm import Session
from app import models, schemas

def get_user(db: Session, student_id: str, name: str, phone: str):
    return db.query(models.User).filter_by(
        student_id=student_id, name=name, phone=phone
    ).first()

def create_reservation(db: Session, user_id: int, data: schemas.ReservationCreate):
    reservation = models.Reservation(
        user_id=user_id,
        room_id=data.room_id,
        start_time=data.start_time,
        end_time=data.end_time,
        status="reserved"
    )
    db.add(reservation)
    db.commit()
    db.refresh(reservation)
    return reservation
