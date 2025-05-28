from fastapi import APIRouter, Form, Depends, Request
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from app import crud, jwt_handler, database

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# DB 세션 의존성 주입 함수
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET 요청: 로그인 폼 렌더링
@router.get("/login")
def show_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# 로그인 요청을 처리하는 API
@router.post("/login")
def login(
        request: Request,
        student_id: str = Form(...),  # 폼에서 받은 학번
        name: str = Form(...),        # 이름
        phone: str = Form(...),       # 전화번호
        db: Session = Depends(get_db)
):
    # DB에서 유저 정보 확인
    user = crud.get_user(db, student_id, name, phone)
    if user:
        # JWT 토큰 발급
        token = jwt_handler.create_token(user.id)

        # 로그인 성공 시 예약 페이지로 리디렉션 + 쿠키에 토큰 저장
        response = RedirectResponse(url="/reservation", status_code=302)
        response.set_cookie(key="token", value=token)
        return response

    # 로그인 실패 시 다시 로그인 페이지로
    return templates.TemplateResponse("login.html", {
        "request": request,
        "error": "로그인 정보가 올바르지 않습니다."
    })
