from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from app.database import Base
import enum

class StatusEnum(str, enum.Enum):
    reserved = "reserved"
    in_use = "in_use"
    exited = "exited"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String(20), unique=True, index=True)
    name = Column(String(50))
    phone = Column(String(20))

class Reservation(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    room_id = Column(String(10))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    status = Column(Enum(StatusEnum))
