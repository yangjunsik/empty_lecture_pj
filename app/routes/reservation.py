from fastapi import APIRouter, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from datetime import datetime

from app import database, jwt_handler, crud, schemas

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# DB 세션 의존성
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 예약 페이지 렌더링
@router.get("/reservation")
def show_reservation_page(request: Request):
    return templates.TemplateResponse("reservation.html", {"request": request})

# 시간 선택 페이지 렌더링
@router.get("/reservation/time")
def show_time_select_page(request: Request):
    return templates.TemplateResponse("time_select.html", {"request": request})

# 실제 예약 처리 API
@router.post("/reservation/submit")
def submit_reservation(
        request: Request,
        room_id: str = Form(...),
        start_time: str = Form(...),  # yyyy-mm-ddTHH:MM 형식 예상
        end_time: str = Form(...),
        token: str = Form(...),
        db: Session = Depends(get_db)
):
    # 토큰에서 유저 ID 추출
    user_id = jwt_handler.decode_token(token)

    # datetime 형식 변환
    start = datetime.fromisoformat(start_time)
    end = datetime.fromisoformat(end_time)

    # 예약 생성
    data = schemas.ReservationCreate(room_id=room_id, start_time=start, end_time=end)
    crud.create_reservation(db, user_id=user_id, data=data)

    # 예약 완료 화면으로 이동
    return RedirectResponse(url="/reservation/confirmed", status_code=302)

# 예약 완료 페이지 렌더링
@router.get("/reservation/confirmed")
def show_confirmed(request: Request):
    return templates.TemplateResponse("reserved.html", {"request": request})
