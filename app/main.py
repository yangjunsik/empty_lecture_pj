from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from app.routes import auth, reservation
from app.database import engine
from app import models

# 테이블 생성 (MySQL에 테이블 없으면 자동 생성됨)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS 설정 (프론트 개발 시 로컬 연동 허용)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 정적 파일, 템플릿 설정
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# 라우터 등록
app.include_router(auth.router)
app.include_router(reservation.router)

@app.get("/")
def root():
    return RedirectResponse(url="/login")

# 서버 실행 명령어:
# uvicorn app.main:app --reload
