from fastapi import APIRouter, Form, Request, Depends
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from app import crud, database

router = APIRouter()
templates = Jinja2Templates(directory="templates")

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/login")
def show_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login")
def login_user(
        request: Request,
        user_id: str = Form(...),
        name: str = Form(...),
        password: str = Form(...),
        db: Session = Depends(get_db)
):
    user = crud.get_user_for_login(db, user_id=user_id, name=name, password=password)
    if user:
        return templates.TemplateResponse("reserved.html", {"request": request, "user": user})

    return templates.TemplateResponse("login.html", {
        "request": request,
        "error": "로그인 정보가 올바르지 않습니다."
    })
