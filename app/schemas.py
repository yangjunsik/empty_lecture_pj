from pydantic import BaseModel
from datetime import datetime

class UserLogin(BaseModel):
    student_id: str
    name: str
    phone: str

class ReservationCreate(BaseModel):
    room_id: str
    start_time: datetime
    end_time: datetime

class ReservationOut(BaseModel):
    room_id: str
    start_time: datetime
    end_time: datetime
    status: str
